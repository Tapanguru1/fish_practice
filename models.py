
from sqlalchemy import Column,Integer,String,Float
from Database.database import Base
class Product(Base):
    __tablename__='Fish2'
    id=Column(Integer,primary_key=True,index=True)
    Species=Column(String(20))
    Weight=Column(Float)
    Length1=Column(Float)
    Length2=Column(Float)
    Length3= Column(Float)
    Height=Column(Float)
    Width=Column(Float)