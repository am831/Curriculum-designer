from pydantic import BaseSettings

class Settings(BaseSettings):
    database_host: str
    database_port: str 
    database_password: str 
    database_username: str 
    database_name: str 
    secret_key: str 
    algorithm: str
    access_token_exp: int 

    class Config:
        env_file = ".env"  #running alembic from fastapi dir needs "app/.env"

settings = Settings()