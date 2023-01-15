# File name: sqlalchemy_example_mysql.py
# Author: Kevin Rojas
# email: krojas.alfaro7@gmail.com
# Python Version: 3.8
# Ejemplo de conexion con mysql desde Python

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

load_dotenv()
URI_MYSQL = os.getenv('URI_MYSQL')
engine = create_engine(URI_MYSQL, echo=True)
Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)

class Parcela(Base):

    __tablename__ = 'parcela'

    id = Column(Integer, primary_key=True)
    # id_propietario = Column(Integer)
    ref_catastral = Column(String)
    # ref_catast_sub = Column(String)
    # municipio = Column(Integer)
    # num_poligono = Column(Integer)
    # num_parcela = Column(Integer)
    # recinto = Column(String)
    # superficie = Column(Integer)
    # superficie_util = Column(Integer)
    # id_cultivo = Column(Integer)
    # id_variedad = Column(Integer)
    # fecha_cultivo = Column(Integer)
    # marco_x = Column(Integer)
    # marco_y = Column(Integer)
    # espaldera = Column(Integer)
    # tipo_produccion = Column(String)
    # tipo_certificacion = Column(String)
    # diam_contador = Column(Integer)
    # diam_toma = Column(Integer)
    # q_teorico = Column(Float)
    # conjunto_riego = Column(Integer)
    # observacion = Column(String)
    # estacion_asociada = Column(Integer)
    # fecha_creacion = Column(DateTime)
    # fecha_modificacion = Column(DateTime)

    def __repr__(self):
       return "<parcela()>"


class PlataformaUsuario(Base):

    __tablename__ = 'plataforma_usuario'

    id = Column(Integer, primary_key=True)
    n_socio_comunidad = Column(Integer)
    rol_usuario = Column(String)
    nombre = Column(String)
    nickname = Column(String)
    apellido = Column(String)

    def __repr__(self):
       return "<User()>"

print(PlataformaUsuario.__table__)
session = Session()
users = session.query(PlataformaUsuario)

session.commit()
for user in users:
    print(user.rol_usuario)
    print(user.nombre)

# Add register

# new_user = PlataformaUsuario(nombre="PRUEBA PYTHON", nickname="PYTHON")
# session.add(new_user)
# session.commit()
# print(f"Nuevo usuario: {new_user.id}")

# Update register
session = Session()
domain = {'id': 392}
users = session.query(PlataformaUsuario).filter_by(**domain).update({'apellido': '10UPDATE PYT'})
session.commit()


# new_parcela = Parcela(ref_catastral="DESDE PYTHON")
# session.add(new_parcela)
# session.commit()
# print(f"Nueva parcela: {new_parcela.id}")
#
# "Algo don don omar salcefda".split(' ', 1)
