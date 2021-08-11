import sys
sys.path.append("..")

from typing import Optional, List
from fastapi import FastAPI, Depends, HTTPException
import sqlalchemy.orm as _orm
from starlette.responses import RedirectResponse

import app.database as _database
import app.schemas as _schemas
import app.services as _services


app = FastAPI()

_database.create_database()

@app.get('/')
def read_root():
    response = RedirectResponse(url="/docs")
    return response  

@app.get('/colonias/{nombre}', response_model=_schemas.ShowColonia)
def read_colonia(
            nombre: str, 
            db: _orm.Session=Depends(_database.get_db)):
    db_colonia = _services.get_colonia(db=db, nombre=nombre)
    if db_colonia is None:
        raise HTTPException(
            status_code=404, detail='sorry this colonia does not exist'
        )
    return db_colonia

@app.get('/municipio/{nombre}', response_model=_schemas.ShowMunicipio)
def read_municipio(
            nombre: str, 
            db: _orm.Session=Depends(_database.get_db)):
    db_municipio = _services.get_municipio(db=db, nombre=nombre)
    if db_municipio is None:
        raise HTTPException(
            status_code=404, detail='sorry this municipio does not exist'
        )
    return db_municipio


@app.get('/municipio', response_model=List[_schemas.ShowMunicipio])
def read_municipios(
            skip: int=0, 
            limit: int=10, 
            db: _orm.Session=Depends(_database.get_db)):
    municipios = _services.get_municipios(db=db, skip=skip, limit=limit)
    return municipios