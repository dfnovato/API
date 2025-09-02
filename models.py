from sqlalchemy import Column, Integer, String, Float
from database import Base

id_filme = Column(Integer, primary_key=True, index=True, autoincrement=True)
titulo = Column(String(50), index = True)
genero = Column(String(50), index = True)
ano = Column(Integer)
nota = Column(Float)