from datetime import timedelta

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app import database
from app.routers import admin, login


ACCESS_TOKEN_EXPIRE_MINUTES = 30  


app = FastAPI()

database.create_database()


app.include_router(login.router)
app.include_router(admin.router)


@app.get('/')
def read_root():
    response = RedirectResponse(url="/docs")
    return response