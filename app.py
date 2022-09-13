import numpy as np
from fastapi import FastAPI,Depends,Query
from Database.database import engine 
from sqlalchemy.orm import Session
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 
from pydantic import BaseModel

from fastapi import FastAPI
import models
from Database.database import engine 


models.Base.metadata.create_all(engine)


from Database.database import SessionLocal
app=FastAPI()
@app.get('/')
def index():
    return {'message': 'Hello World'}
class request_body(BaseModel):
    Weight: float
    Length1:float
    Length2:float
    Length3: float
    Height: float
    Width:float



dataset=pd.read_csv("fish.csv")
dataset.head()
X=dataset.iloc[:,1:7].values
y=dataset.iloc[:,0].values
X_train, X_test,y_train,y_test=train_test_split(X,y,test_size=0.5,random_state=0)
regression=LogisticRegression(solver='lbfgs',max_iter=1000)
regression.fit(X_train,y_train)
def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()



@app.post('/predict')
def predict(data : request_body, db: Session= Depends(get_db)):
    test_model=models.Product()
    test_data=[[
        data.Weight,
        data.Length1,
        data.Length2,
        data.Length3,
        data.Height,
        data.Width]]
    y_pred=regression.predict(test_data)[0]
    test_model.Species=y_pred
    test_model.Weight=data.Weight
    test_model.Length1=data.Length1
    test_model.Length2=data.Length2
    test_model.Length3=data.Length3
    test_model.Height=data.Height
    test_model.Width=data.Width
    db.add(test_model)
    db.commit()
    return y_pred