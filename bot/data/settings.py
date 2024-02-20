from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    token: str = None
    rate_limit: float = 0.7


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)