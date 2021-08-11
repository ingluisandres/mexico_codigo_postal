from typing import List, Optional
from fastapi import Body, Query
from pydantic import BaseModel


class Colonia(BaseModel):
    d_codigo: str
    d_asenta: str
    d_tipo_asenta: str 
    D_mnpio: str
    d_estado: str
    d_CP: str
    c_estado:str
    c_CP:str
    c_tipo_asenta:str
    c_mnpio:str
    id_asenta_cpcons:str
    d_zona:str
    c_cve_ciudad:str
    class Config():
        orm_mode = True

class ShowColonia(Colonia):
    id:int
    class Config():
        orm_mode = True


class Municipio(BaseModel):
    D_mnpio : str
    c_mnpio : str
    d_estado: str
    c_estado: str
    class Config():
        orm_mode = True


class ShowMunicipio(Municipio):
    id:int
    class Config():
        orm_mode = True