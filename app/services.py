import sqlalchemy.orm as _orm
import app.models as _models
import app.schemas as _schemas


def get_colonia(db: _orm.Session, nombre:str):
    return db.query(_models.Colonia).filter(_models.Colonia.d_asenta == nombre).all()

def get_colonia_by_cp(db: _orm.Session, cp:str):
    return db.query(_models.Colonia).filter(_models.Colonia.d_codigo == cp).all()

def create_colonia(db: _orm.Session, colonia: _schemas.Colonia):
    db_colonia = _models.Colonia(
        d_codigo= colonia.d_codigo,
        d_asenta=colonia.d_asenta,
        d_tipo_asenta=colonia.d_tipo_asenta,
        D_mnpio=colonia.D_mnpio,
        d_estado=colonia.d_estado,
        d_CP=colonia.d_CP,
        c_estado=colonia.c_estado,
        c_CP=colonia.c_CP,
        c_tipo_asenta=colonia.c_tipo_asenta,
        c_mnpio=colonia.c_mnpio,
        id_asenta_cpcons=colonia.id_asenta_cpcons,
        d_zona=colonia.d_zona,
        c_cve_ciudad=colonia.c_cve_ciudad
    )
    db.add(db_colonia)
    db.commit()
    db.refresh(db_colonia)
    return db_colonia


def get_municipio(db: _orm.Session, nombre:str):
    return db.query(_models.Municipio).filter(_models.Municipio.D_mnpio == nombre).all()

def get_municipios(db:_orm.Session, skip:int, limit:int):
    return db.query(_models.Municipio).offset(skip).limit(limit).all()


def get_estado(db: _orm.Session, nombre:str):
    return db.query(_models.Estado).filter(_models.Estado.d_estado == nombre).first()