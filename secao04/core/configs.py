""" configurações """
from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://myuser:mypassword@localhost:5432/famp'
    DBBaseModel: ClassVar = declarative_base()

    class Config:
        """ config """
        case_sensitive = True

settings = Settings()
