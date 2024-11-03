from pydantic  import  BaseModel,EmailStr,Field
from typing import Optional,List


class RoleCreate(BaseModel):
    role_name: str
    access_modules: List[str]
    active: bool= True
 

class UserCreate(BaseModel):
    first_name: str        
    last_name: str
    email: EmailStr      
    password: str
    role_id :int


class show_blog_user(BaseModel):
    role_name:str
    access_modules:str
    class Config:
        orm_mode=True

class show_user(BaseModel):
    id:int 
    email:str
    role_id :int
    role:show_blog_user 

    class Config:
        orm_mode=True

class show_user_role(BaseModel):
    id:int 
    email:str
    class Config:
        orm_mode=True


class Showrole(BaseModel):
    id:int
    role_name: str
    access_modules: str
    creator:List[show_user_role] =[]

    class Config:
        orm_mode=True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Login(BaseModel):
    email:str
    password:str 

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None
