from app.config import Base,engine
from fastapi import FastAPI
from app.router import auth,role


Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(role.router)
app.include_router(auth.myrouter)
