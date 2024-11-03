from sqlalchemy.orm import Session
from app import models,schemas
from passlib.context import CryptContext


pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")


def create_role(db:Session,role:schemas.RoleCreate):
    db_role = models.Role(
    role_name=role.role_name,
    access_modules=",".join(role.access_modules),
    active=role.active)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)

    return db_role


def get_role(db: Session,search:str=None):
    if search:
        return db.query(models.Role).filter(models.Role.role_name.like(f"%{search}%")).all()
    return  db.query(models.Role).all()
 

def create_user(db:Session,user:schemas.UserCreate):
    hased_password=pwd_context.hash(user.password)

    db_user= models.User(
        first_name= user.first_name,
        last_name= user.last_name,
        email= user.email,
        role_id= user.role_id,
        password=hased_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def Get_user(db: Session,email:str=None):
    if email:
        return db.query(models.User).filter(models.User.email.like(f"%{email}%")).all()
    return db.query(models.User).all()


def get_user_by_email(db: Session,email: str):
    return db.query(models.User).filter(models.User.email == email).first()


