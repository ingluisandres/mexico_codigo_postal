from  sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

import app.database as _database


class Estado(_database.Base):
    __tablename__ = "estados"
    id = Column(Integer, primary_key=True, index=True)
    d_estado = Column(String, index=True)

    municipios_list = relationship('Municipio', back_populates='estado')


class Municipio(_database.Base):
    __tablename__ = "municipios"
    id = Column(Integer, primary_key=True, index=True)
    D_mnpio = Column(String, index=True)
    c_mnpio = Column(String, index=True)
    d_estado = Column(String, index= True)
    c_estado = Column(Integer, ForeignKey('estados.id'))

    estado = relationship('Estado', back_populates='municipios_list')
    colonias_list = relationship('Colonia', back_populates='municipio')


class Colonia(_database.Base):
    __tablename__ = "colonias"
    id = Column(Integer, primary_key=True, index=True)
    d_codigo=  Column(Integer, index= True)
    d_asenta=  Column(String, index= True)
    d_tipo_asenta=  Column(String, index= True) 
    D_mnipio=  Column(String, index= True)
    d_estado=  Column(String, index= True)
    c_estado=  Column(Integer, index= True)
    c_tipo_asenta=  Column(Integer, index= True)
    c_mnpio=  Column(Integer, index= True)
    id_asenta_cpcons=  Column(Integer, index= True)
    d_zona=  Column(String, index= True)
    id_municipio = Column(Integer, ForeignKey('municipios.id'))

    municipio = relationship('Municipio', back_populates='colonias_list')


class Admin(_database.Base):
    __tablename__ = "admins"
    id = Column(Integer, primary_key=True, index=True)
    admin_name =  Column(String, index=True)
    password =  Column(String, index=True)