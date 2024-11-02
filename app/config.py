import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Sessting(BaseSettings):
    SECRETKEY: str= os.getenv("SECRETKEY")
    ALGORITHM: str =os.getenv("ALGORITHM") 
    ACCESS_TOKEN_EXPIRE_MINUTES: int= int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

setting=Sessting()

database_url=os.getenv("DATABASE_URL")
engine=create_engine(
    database_url,connect_args={"check_same_thread":False})

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()    