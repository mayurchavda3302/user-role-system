from fastapi import APIRouter,Depends
from sqlalchemy.orm  import Session
from app import crud,schemas
from  app.config import get_db
from ..oauth2 import oauth_shema

router= APIRouter(
    prefix="/roles",
    tags=["roles"]
)

@router.post("/create_role")
async def create_role(role: schemas.RoleCreate, db: Session= Depends(get_db),user=Depends(oauth_shema)):
    return crud.create_role(db=db,role=role)

@router.get("/get_role",response_model=list[schemas.Showrole])
async def get_role(searh:str=None ,db: Session= Depends(get_db),user=Depends(oauth_shema)):
    return crud.get_role(db,searh)
