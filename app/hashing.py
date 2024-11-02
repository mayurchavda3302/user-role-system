from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


def  bcrypt(password:str):
    return pwd_cxt.hash(password)

def  verify(plain_pass,hased_pass):
    return pwd_cxt.verify(plain_pass,hased_pass)

