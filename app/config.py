from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    database_details: str
    class Config:
        env_file= ".env"


settings = Settings()