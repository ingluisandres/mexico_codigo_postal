from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import JWTError, jwt

from app.schemas import schemas
from app.config import database, models
from app.services import services


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_admin(db: Session=Depends(database.get_db), token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        admin = db.query(models.Admin).get(payload["sub"])
    except:
        raise HTTPException(status_code=401, detail="Invalid Email or Password")
    return db.query(models.Admin).filter(models.Admin.admin_name == payload["sub"]).first()


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


def login(db: Session, admin: schemas.Login):
    admin = db.query(models.Admin).filter(models.Admin.admin_name == admin.username).first()
    return admin

def verify_password(plain_password, hashed_password):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(data, credentials_exception)

def verify_token(data:str, credentials_exception):
    try:
        payload = jwt.decode(data, SECRET_KEY, algorithms=[ALGORITHM])
        admin_name: str = payload.get("sub")
        if admin_name is None:
            raise credentials_exception
        token_data = schemas.TokenData(admin_name=admin_name)
    except JWTError:
        raise credentials_exception