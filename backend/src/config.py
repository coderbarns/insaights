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

    ES_SCHEME: str = "http"
    ES_PORT: int = 9200
    ES_HOST: str = "localhost"
    ES_USER: str = ""
    ES_PASSWORD: str = ""

    EMBEDDINGS_PATH: str = "embeddings"

    def get_pg_connection_uri(self):
        return f"{self.POSTGRES_SCHEME}://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    def get_es_connection_uri(self):
        if self.ES_USER == "" or self.ES_PASSWORD == "":
            return f"{self.ES_SCHEME}://{self.ES_HOST}:{self.ES_PORT}"
        return f"{self.ES_SCHEME}://{self.ES_USER}:{self.ES_PASSWORD}@{self.ES_HOST}:{self.ES_PORT}"


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
