from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime,timedelta
from app.config import Base
from passlib.context import CryptContext
from datetime import datetime

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String(40), unique=True, nullable=False)
    access_modules = Column(String)  
    created_at = Column(DateTime, default=datetime.utcnow)
    active = Column(Boolean, default=True)
    
    user = relationship("User", back_populates="role", lazy='noload')  #  unnecessary recursion



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(20), index=True)
    last_name = Column(String(20), index=True)
    email = Column(String(25), index=True, unique=True, nullable=False)
    password = Column(String(100), nullable=False) 
    role_id = Column(Integer, ForeignKey('roles.id'))

    role = relationship("Role", back_populates="user", lazy='noload')