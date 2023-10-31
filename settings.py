from pathlib import Path
from pydantic_settings import BaseSettings

# All .env variable should match with variable in class below. no less or extra, will throw forbidden
class Settings(BaseSettings):
    DB_NAME: str
    DB_HOST: str
    DB_USER: str
    DB_PASS: str
    DB_PORT: str

    # Bypass forbidden error not matching var with .env
    class Config:
      extra = "ignore"

settings = Settings(_env_file=Path(__file__).parent/ ".env", _env_file_encoding="utf-8")