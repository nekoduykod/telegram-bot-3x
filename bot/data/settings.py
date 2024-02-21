''' I took this snippet from https://github.com/DOFER998/aiogram-bot-template/blob/main/src/data/settings.py
    check middlewares/throttling.py where current module imported.'''
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    token: str = None
    rate_limit: float = 0.7


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)