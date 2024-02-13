from typing import Optional
from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    
    @validator('titulo')
    def validar_titulo(cls, value: str):
        """ validação do titulo """
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O titulo deve ter pelo menos 3 palavras')
        
        if value.islower():
            raise ValueError('O titulo deve ser capitalizado.')
        
        return value
    
    @validator('aulas')
    def validar_aulas(cls, value: int):
        """ validação do aulas """
        
        if value < 12:
            raise ValueError('A quantidade de aulas deve ser maior que 12')
        return value
    
    @validator('horas')
    def validar_horas(cls, value: int):
        """ validação do horas """
        
        if value < 10:
            raise ValueError('A quantidade de horas deve ser maior que 10')
        return value
    
    
Cursos = [
    Curso(id=1, titulo='Programação estruturada 1', aulas=42, horas=56),
    Curso(id=2, titulo='Programação estruturada 2', aulas=52, horas=66),
    Curso(id=3, titulo='Programação estruturada 3', aulas=62, horas=76),
    Curso(id=4, titulo='Programação estruturada 4', aulas=72, horas=86),
    Curso(id=5, titulo='Programação estruturada 5', aulas=82, horas=96),
    Curso(id=6, titulo='Programação estruturada 6', aulas=92, horas=16)
]
