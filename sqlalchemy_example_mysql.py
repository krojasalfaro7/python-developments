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


class PlataformaUsuario(Base):

    __tablename__ = 'plataforma_usuario'

    id = Column(Integer, primary_key=True)
    n_socio_comunidad = Column(Integer)
    rol_usuario = Column(String)
    nombre = Column(String)
    nickname = Column(String)

    def __repr__(self):
       return "<User()>"

print(PlataformaUsuario.__table__)
session = Session()
users = session.query(PlataformaUsuario)

session.commit()
for user in users:
    print(user.rol_usuario)
    print(user.nombre)
