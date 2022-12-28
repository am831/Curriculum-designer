from pydantic import BaseSettings

class Settings(BaseSettings):
    database_host: str
    database_port: str 
    database_password: str 
    database_username: str 
    database_name: str 
    #any string of random characters
    secret_key: str 
    #recommended: HS256
    algorithm: str
    #access token expiration time in minutes
    access_token_exp: int

    class Config:
        env_file = ".env"  #running alembic from fastapi dir needs "app/.env"

settings = Settings()