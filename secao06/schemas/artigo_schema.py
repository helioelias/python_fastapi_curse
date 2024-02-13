""" imports """
from typing import Optional

from pydantic import BaseModel, HttpUrl

class ArtigoSchema(BaseModel):
    """
    Artigos
    """
    id: Optional[int] = None
    titulo: str
    descricao: str
    url_fonte: HttpUrl
    usuario_id: Optional[int] = None
    
    class ConfigDict:
        """
        Config
        """
        from_attributes = True
    
