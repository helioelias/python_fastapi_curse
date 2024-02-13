""" imports """

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://myuser:mypassword@localhost:5432/famp'
    
    class Config:
        case_sensitive = True
        
settings: Settings = Settings()