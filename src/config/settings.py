from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str
    app_version: str
    app_env: str
    debug: bool

    host: str
    port: int

    database_url: str

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()