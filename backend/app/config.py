from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    allowed_origins: str = "http://localhost:5173,http://localhost:3000"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False
    )

settings = Config()