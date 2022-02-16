from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    database_url: str
    class Config:
        env_file= ".env"


settings = Settings()