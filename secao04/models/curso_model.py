""" imports """
from typing import ClassVar

from core.configs import settings

from sqlalchemy import Column, Integer, String

class CursoModel(settings.DBBaseModel):
    __tablename__ = 'cursos'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)
    
    def __init__(self, titulo, aulas, horas):
      self.titulo = titulo
      self.aulas = aulas
      self.horas = horas