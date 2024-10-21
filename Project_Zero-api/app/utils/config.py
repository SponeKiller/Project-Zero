import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: str
    refresh_token_expire_minutes: str
    refresh_token_length: str
    csrf_token_length: str
    pwd_context_scheme: str

    class Config:
        env_file = os.getenv("Project_Zero-api/.env")
        
settings = Settings()