import sys
sys.path.append("..")

from fastapi import FastAPI

from app.config import database
from app.routers import admin, login


app = FastAPI()

database.create_database()

app.include_router(login.router)
app.include_router(admin.router)


@app.get('/')
def read_root():
    return {"Luis Contreras":"FastAPI - MYSQL"}