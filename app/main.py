from datetime import timedelta

from fastapi import FastAPI
from starlette.responses import RedirectResponse

import database
from routers import admin, login


app = FastAPI()

database.create_database()


app.include_router(login.router)
app.include_router(admin.router)


@app.get('/')
def read_root():
    response = RedirectResponse(url="/docs")
    return response