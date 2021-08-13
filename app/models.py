import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import datetime as _dt

import app.database as _database


class Estado(_database.Base):
    __tablename__ = "estados"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    d_estado = _sql.Column(_sql.String, index=True)

    municipios_list = _orm.relationship('Municipio', back_populates='estado')


class Municipio(_database.Base):
    __tablename__ = "municipios"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    D_mnpio = _sql.Column(_sql.String, index=True)
    c_mnpio = _sql.Column(_sql.String, index=True)
    d_estado = _sql.Column(_sql.String, index= True)
    c_estado = _sql.Column(_sql.Integer, _sql.ForeignKey('estados.id'))

    estado = _orm.relationship('Estado', back_populates='municipios_list')
    colonias_list = _orm.relationship('Colonia', back_populates='municipio')



class Colonia(_database.Base):
    __tablename__ = "colonias"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    d_codigo=  _sql.Column(_sql.Integer, index= True)
    d_asenta=  _sql.Column(_sql.String, index= True)
    d_tipo_asenta=  _sql.Column(_sql.String, index= True) 
    D_mnipio=  _sql.Column(_sql.String, index= True)
    d_estado=  _sql.Column(_sql.String, index= True)
    c_estado=  _sql.Column(_sql.Integer, index= True)
    c_tipo_asenta=  _sql.Column(_sql.Integer, index= True)
    c_mnpio=  _sql.Column(_sql.Integer, index= True)
    id_asenta_cpcons=  _sql.Column(_sql.Integer, index= True)
    d_zona=  _sql.Column(_sql.String, index= True)
    id_municipio = _sql.Column(_sql.Integer, _sql.ForeignKey('municipios.id'))

    municipio = _orm.relationship('Municipio', back_populates='colonias_list')
    