""" imports """
from typing import Optional

from pydantic import BaseModel as SCBaseModel

class CursoSchema(SCBaseModel):
    """
    Cursos
    """
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    
    class ConfigDict:
        """
        Config
        """
        #from_attributes = True
        from_attributes = True
    