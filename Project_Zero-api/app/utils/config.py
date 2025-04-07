import os

from pydantic_settings import BaseSettings, SettingsConfigDict 
from pathlib import Path

ABS_DIR = Path(__file__).resolve().parent.parent
APP_ENV = os.getenv("APP_ENV", "development")

# Loaded file definition
ENV_FILES = [".env", f".env.{APP_ENV}.local", f".env.{APP_ENV}"]

env_files = [os.path.join(ABS_DIR, file) for file in ENV_FILES]
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
    cors_allow_origins: str
    cors_allow_methods: str
    cors_allow_headers: str
    sentry_dsn: str
    openai_api_key: str
    openai_model: str

    model_config = SettingsConfigDict(env_file=env_files,
                                      env_file_encoding="utf-8",
                                      case_sensitive=False,
                                      extra = "ignore")
        
settings = Settings()