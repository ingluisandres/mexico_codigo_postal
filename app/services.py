from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app import models, schemas


def get_colonia(db: Session, nombre:str):
    return db.query(models.Colonia).filter(models.Colonia.d_asenta == nombre).all()

def get_colonia_by_cp(db: Session, cp:str):
    return db.query(models.Colonia).filter(models.Colonia.d_codigo == cp).all()

def create_colonia(db: Session, colonia: schemas.Colonia):
    db_colonia = models.Colonia(
        d_codigo= colonia.d_codigo,
        d_asenta=colonia.d_asenta,
        d_tipo_asenta=colonia.d_tipo_asenta,
        D_mnipio=colonia.D_mnipio,
        d_estado=colonia.d_estado,
        c_estado=colonia.c_estado,
        c_tipo_asenta=colonia.c_tipo_asenta,
        c_mnpio=colonia.c_mnpio,
        id_asenta_cpcons=colonia.id_asenta_cpcons,
        d_zona=colonia.d_zona
    )
    db.add(db_colonia)
    db.commit()
    db.refresh(db_colonia)
    return db_colonia


def get_municipio(db: Session, nombre:str):
    return db.query(models.Municipio).filter(models.Municipio.D_mnpio == nombre).all()

def get_municipios(db:Session, skip:int, limit:int):
    return db.query(models.Municipio).offset(skip).limit(limit).all()


def get_estado(db: Session, nombre:str):
    return db.query(models.Estado).filter(models.Estado.d_estado == nombre).first()


def create_admin(db: Session, admin: schemas.Admin):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_password = pwd_context.hash(admin.password)
    db_admin = models.Admin(
        admin_name= admin.admin_name,
        password=hashed_password
    )
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin