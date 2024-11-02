from app import JWT_token
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer

oauth_shema= OAuth2PasswordBearer(tokenUrl="login")

def user(data:str=Depends(oauth_shema)):
   credentials_exception=(
      HTTPException(
         status_code=status.HTTP_401_UNAUTHORIZED,
         detail="unuthorize"
      )

   )
   return JWT_token.verify_token(data,credentials_exception)