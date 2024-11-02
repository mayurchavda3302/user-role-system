from fastapi import APIRouter,HTTPException,Depends,status
from sqlalchemy.orm import Session
from app.config import setting,get_db
from app import  models,JWT_token,hashing,schemas,crud,oauth2
from fastapi.security import OAuth2PasswordRequestForm

ALGORITHM=setting.ALGORITHM
SECRETKEY=setting.SECRETKEY

myrouter = APIRouter(
    tags=["Authantication"],
    prefix="/user"
)


@myrouter.post("/login")
def Login(request:OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
      user=db.query(models.User).filter(models.User.email == request.username).first()
      if not user:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detail="User not found")
      if not hashing.verify(request.password,user.password):
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detail="Incorrect password")
      access_token=JWT_token.create_access_token(data={"sub":user.email})
      return {"acess Token":access_token,"Token Type":"bearer"}
           


@myrouter.post("/signup")
def singup(user: schemas.UserCreate,db:Session=Depends(get_db),req=Depends(oauth2.oauth_shema)):
    existing_user=crud.get_user_by_email(db,user.email)
    if existing_user:
         raise HTTPException(
              status_code=404,
              detail=f"user with this  email : {user.email}  aldery in database")
    new_user=crud.create_user(db,user)
    return {"user created successfully ":new_user}
  

@myrouter.get("/get_user")
def get_user(search_id:int= None,email:str=None,db:Session=Depends(get_db),req=Depends(oauth2.oauth_shema)):
    return crud.Get_user(db,search_id,email)


