import sqlalchemy.orm as _orm
import app.models as _models

def get_colonia(db: _orm.Session, nombre:str):
    return db.query(_models.Colonia).filter(_models.Colonia.d_asenta == nombre).first()


def get_municipio(db: _orm.Session, nombre:str):
    return db.query(_models.Municipio).filter(_models.Municipio.D_mnpio == nombre).first()

def get_municipios(db:_orm.Session, skip:int, limit:int):
    return db.query(_models.Municipio).offset(skip).limit(limit).all()


def get_estado(db: _orm.Session, nombre:str):
    return db.query(_models.Estado).filter(_models.Estado.d_estado == nombre).first()