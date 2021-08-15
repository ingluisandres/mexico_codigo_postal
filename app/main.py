from typing import Optional, List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from app import database, schemas, services


app = FastAPI()

database.create_database()


@app.get('/')
def read_root():
    response = RedirectResponse(url="/docs")
    return response  

@app.get('/colonias/{nombre}', response_model=List[schemas.ShowColonia])
def read_colonia(
            nombre: str, 
            db: Session=Depends(database.get_db)):
    db_colonia = services.get_colonia(db=db, nombre=nombre)

    if db_colonia is None:
        raise HTTPException(
            status_code=404, detail='sorry this colonia does not exist'
        )
    return db_colonia

@app.get('/colonias/cp/{cp}', response_model=List[schemas.ShowColonia])
def read_colonia_by_cp(
            cp: str, 
            db: Session=Depends(database.get_db)):
    db_colonia = services.get_colonia_by_cp(db=db, cp=cp)
    if db_colonia is None:
        raise HTTPException(
            status_code=404, detail='sorry this colonia does not exist'
        )
    return db_colonia

@app.post('/colonias', response_model=schemas.ShowColonia)
def create(colonia: schemas.Colonia, db: Session=Depends(database.get_db)):
    return services.create_colonia(db=db, colonia=colonia)


@app.get('/municipio/{nombre}', response_model=List[schemas.ShowMunicipio])
def read_municipio(
            nombre: str, 
            db: Session=Depends(database.get_db)):
    db_municipio = services.get_municipio(db=db, nombre=nombre)
    if db_municipio is None:
        raise HTTPException(
            status_code=404, detail='sorry this municipio does not exist'
        )
    return db_municipio

@app.get('/municipio', response_model=List[schemas.ShowAllMunicipios])
def read_municipios(
            skip: int=0, 
            limit: int=10, 
            db: Session=Depends(database.get_db)):
    municipios = services.get_municipios(db=db, skip=skip, limit=limit)
    return municipios


@app.get('/estado/{nombre}', response_model=schemas.ShowEstado)
def read_estado(
            nombre: str, 
            db: Session=Depends(database.get_db)):
    db_estado = services.get_estado(db=db, nombre=nombre)
    if db_estado is None:
        raise HTTPException(
            status_code=404, detail='sorry this estado does not exist'
        )
    return db_estado


@app.post('/admin', response_model=schemas.ShowAdmin)
def create_admin(admin: schemas.Admin, db: Session=Depends(database.get_db)):
    return services.create_admin(db=db, admin=admin)