from app.config import setting,get_db
from datetime import datetime,timedelta,timezone
from jose import jwt,JWSError
from .import schemas

SECRETKEY=setting.SECRETKEY
ALGORITHM=setting.ALGORITHM
time=setting.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    try:
        to_encode=data.copy()
        expire= datetime.now(timezone.utc) + timedelta(minutes=time)
        to_encode.update({"exp":expire})
        encoded_jwt = jwt.encode(to_encode,SECRETKEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    except JWSError as e:
        # print(e)
        raise e


def verify_token(token:str,credentials_exception):
    try:
        playload=jwt.decode(token,SECRETKEY,algorithms=[ALGORITHM])
        email:str=playload.get("sub") 
        if email is None:
            raise credentials_exception
        token_data=schemas.TokenData(email=email)
        return token_data
    except JWSError:
        # print(e
        raise credentials_exception
