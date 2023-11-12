from pydantic import BaseModel
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Scraip API"

    API_V1_ENDPOINT: str = "/api/v1"

    LOG_LEVEL: str = "INFO"

    POSTGRES_SCHEME: str = "postgresql+psycopg2"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = "5434"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "scraip"

    EMBEDDINGS_PATH: str = "embeddings"

    OPENAI_KEY: str = ""
    GOOGLE_KEY: str = ""
    GOOGLE_CX: str = ""
    YLE_APP_KEY: str = ""

    def get_pg_connection_uri(self):
        return f"{self.POSTGRES_SCHEME}://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


settings = Settings()


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "app"
    LOG_FORMAT: str = "%(levelprefix)s %(asctime)s - %(message)s"
    LOG_LEVEL: str = settings.LOG_LEVEL

    # Logging config
    version: int = 1
    disable_existing_loggers: bool = False
    formatters: dict = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers: dict = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers: dict = {
        LOGGER_NAME: {"handlers": ["default"], "level": LOG_LEVEL},
        "uvicorn": {"handlers": ["default"], "level": LOG_LEVEL},
    }


log_config = LogConfig()
