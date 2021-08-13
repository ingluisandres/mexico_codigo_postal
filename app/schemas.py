from typing import List, Optional
from fastapi import Body, Query
from pydantic import BaseModel


class Colonia(BaseModel):
    d_codigo: int
    d_asenta: str
    d_tipo_asenta: str 
    D_mnipio: str
    d_estado: str
    c_estado: int 
    c_tipo_asenta:int
    c_mnpio: int
    id_asenta_cpcons:int
    d_zona:str
    class Config():
        orm_mode = True

class ShowColonia(Colonia):
    id:int
    class Config():
        orm_mode = True


class Municipio(BaseModel):
    D_mnpio : str
    c_mnpio : int
    d_estado: str
    c_estado: int
    class Config():
        orm_mode = True

class ShowColoniaInMunicipio(BaseModel):
    id:int
    d_codigo: int
    d_asenta: str
    d_tipo_asenta: str 
    c_tipo_asenta:int
    id_asenta_cpcons:int
    d_zona:str
    class Config():
        orm_mode = True

class ShowMunicipio(Municipio):
    id:int
    
    colonias_list: List[ShowColoniaInMunicipio]
    class Config():
        orm_mode = True

class ShowAllMunicipios(BaseModel):
    id:int
    D_mnpio : str
    c_mnpio : int
    d_estado: str
    c_estado: int
    class Config():
        orm_mode = True


class Estado(BaseModel):
    d_estado: str
    class Config():
        orm_mode = True

class ShowMunicipioInEstado(BaseModel):
    id:int
    D_mnpio : str
    c_mnpio : int
    class Config():
        orm_mode = True

class ShowEstado(Estado):
    id:int
    municipios_list: List[ShowMunicipioInEstado]
    class Config():
        orm_mode = True    