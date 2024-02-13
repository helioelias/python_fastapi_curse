""" imports """
from typing import ClassVar
from typing import List

from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://myuser:mypassword@localhost:5432/famp'
    DBBaseModel: ClassVar = declarative_base()
    
    JWT_SECRET: str = '7MPshxEj-MKMaOGYzgor0Sp-5PSNKmjXaNPziEDtC5o'
    """
    import secrets
    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'
    
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        case_sensitive = True
        
settings: Settings = Settings()
