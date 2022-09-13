from sqlalchemy import create_engine,engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import urllib

host_server = os.environ.get('host_server','fishpractice.mysql.database.azure.com' )
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', 3306)))
database_name = os.environ.get('database_name', 'fishpractice')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'tapanguru12@fishpractice')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'Fish@123')))
SQLALCHEMY_DATABASE_URL='mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(db_username,db_password,host_server,db_server_port,database_name)

#SQLALCHEMY_DATABASE_URL='sqlite:///./product.db'

engine= create_engine(SQLALCHEMY_DATABASE_URL,pool_size=3,max_overflow=0
#connect_args={"check_same_thread":False}
)

SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base=declarative_base()