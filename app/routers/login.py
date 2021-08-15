from datetime import timedelta

from fastapi import APIRouter
from typing import Optional, List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, database, services


router = APIRouter(
    prefix="/login",
    tags=["login"]
)


ACCESS_TOKEN_EXPIRE_MINUTES = 30  


@router.post('/')
def login(admin: schemas.Login, db: Session=Depends(database.get_db)):
    user_admin = services.login(db=db, admin=admin)
    if not user_admin:
        raise HTTPException(
            status_code=404, detail='Invalid Credentials'
        )
    if not services.verify_password(admin.password, user_admin.password):
        raise HTTPException(
            status_code=404, detail='Incorrect admin name or password'
        )      
    # generate a jwd token ---------------------

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = services.create_access_token(
        data={"sub": user_admin.admin_name}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}