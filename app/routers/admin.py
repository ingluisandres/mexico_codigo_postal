from fastapi import APIRouter
from typing import Optional, List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, database, services


router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

@router.get('/colonias/{nombre}', response_model=List[schemas.ShowColonia])
def read_colonia(
            nombre: str, 
            db: Session=Depends(database.get_db),
            current_user: schemas.Admin = Depends(services.get_current_user)
    ):
    db_colonia = services.get_colonia(db=db, nombre=nombre)

    if db_colonia is None:
        raise HTTPException(
            status_code=404, detail='sorry this colonia does not exist'
        )
    return db_colonia

@router.get('/colonias/cp/{cp}', response_model=List[schemas.ShowColonia])
def read_colonia_by_cp(
            cp: str, 
            db: Session=Depends(database.get_db),
            current_user: schemas.Admin = Depends(services.get_current_user)):
    db_colonia = services.get_colonia_by_cp(db=db, cp=cp)
    if db_colonia is None:
        raise HTTPException(
            status_code=404, detail='sorry this colonia does not exist'
        )
    return db_colonia

@router.post('/colonias', response_model=schemas.ShowColonia)
def create_colonia(colonia: schemas.Colonia, db: Session=Depends(database.get_db),
current_user: schemas.Admin = Depends(services.get_current_user)):
    return services.create_colonia(db=db, colonia=colonia)


@router.get('/municipio/{nombre}', response_model=List[schemas.ShowMunicipio])
def read_municipio(
            nombre: str, 
            db: Session=Depends(database.get_db),
            current_user: schemas.Admin = Depends(services.get_current_user)):
    db_municipio = services.get_municipio(db=db, nombre=nombre)
    if db_municipio is None:
        raise HTTPException(
            status_code=404, detail='sorry this municipio does not exist'
        )
    return db_municipio


@router.get('/estado/{nombre}', response_model=schemas.ShowEstado)
def read_estado(
            nombre: str, 
            db: Session=Depends(database.get_db),
            current_user: schemas.Admin = Depends(services.get_current_user)):
    db_estado = services.get_estado(db=db, nombre=nombre)
    if db_estado is None:
        raise HTTPException(
            status_code=404, detail='sorry this estado does not exist'
        )
    return db_estado


@router.post('/newadmin', response_model=schemas.ShowAdmin)
def create_admin(admin: schemas.Admin, db: Session=Depends(database.get_db),
current_user: schemas.Admin = Depends(services.get_current_user)):
    return services.create_admin(db=db, admin=admin)

@router.get('/me', response_model=schemas.ShowAdmin)
def get_admin(current_user: schemas.Admin= Depends(services.get_admin)):
    return current_user