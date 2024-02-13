""" imports """
from typing import Optional
from typing import List

from pydantic import BaseModel, EmailStr

from schemas.artigo_schema import ArtigoSchema

class UsuarioSchemaBase(BaseModel):
    """
    Usuarios
    """
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False
    
    class ConfigDict:
        """
        Config
        """
        from_attributes = True
    
class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str

    
class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]
    
class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str] = None
    sobrenome: Optional[str] = None
    email: Optional[str] = None
    senha: Optional[str] = None
    eh_admin: Optional[bool] = False
   