from cgi import test
import numpy as np
from fastapi import FastAPI,Depends,Query
from Database.database import engine 
from sqlalchemy.orm import Session
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from pydantic import BaseModel

from fastapi import FastAPI,HTTPException,status,Request,Form
import models
from Database.database import engine 

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from Database.database import SessionLocal
app=FastAPI()

models.Base.metadata.create_all(engine)

dataset=pd.read_csv("fish.csv")
dataset.head()
X=dataset.iloc[:,1:7].values
y=dataset.iloc[:,0].values

templates = Jinja2Templates(directory="templates")
#X_train, X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
regression=LinearDiscriminantAnalysis(solver='svd',n_components=1)
regression.fit(X,y)
def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()

app.mount("/templates/static", StaticFiles(directory="templates/static"), name="static")

@app.get("/frontend", response_class=HTMLResponse)
async def read_item(request: Request):
    weight = ""
    length1=""
    length2=''
    length3=''
    height=''
    width=''
    species=''

    return templates.TemplateResponse("item.html",context={'request': request, 'weight': weight,'length1':length1,'length2':length2,'length3':length3,'height':height,'width':width,'species':species})

@app.post("/frontend")
def form_post(request: Request, Weight: float = Form(...),Length1:float=Form(...),Length2:float=Form(...),Length3:float=Form(...),Height:float=Form(...),Width:float=Form(...)):
    weight =Weight
    length1=Length1
    length2=Length2
    length3=Length3
    height=Height
    width=Width
    test_data = [[weight, length1, length2,length3, height, width]]
    class_idx=regression.predict(test_data)[0]
    species=class_idx
    
    return templates.TemplateResponse('item.html', context={'request': request, 'weight': weight,'length1':length1,'length2':length2,'length3':length3,'height':height,'width':width,'species':species})


@app.get('/')
def index():
    return {'message': 'Hello World'}

class logistic(BaseModel):
    Weight: float
    Length1: float
    Length2: float
    Length3: float
    Height: float
    Width: float
    Species:str
    

@app.post('/predict')
def predict(data: logistic, db: Session= Depends(get_db)):
    test_model=models.Product()
    test_data=[[
        data.Weight,
        data.Length1,
        data.Length2,
        data.Length3,
        data.Height,
        data.Width]]
    y_pred=regression.predict(test_data)[0]
    data.Species=y_pred
    test_model.Species=y_pred
    test_model.Weight=data.Weight
    test_model.Length1=data.Length1
    test_model.Length2=data.Length2
    test_model.Length3=data.Length3
    test_model.Height=data.Height
    test_model.Width=data.Width
    db.add(test_model)
    db.commit()
    #db.refresh(test_model)
    return y_pred