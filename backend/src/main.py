from dotenv import load_dotenv

load_dotenv(".env")

import logging
import logging.config
from fastapi import FastAPI
from src.config import settings, log_config
from src.api.v1.api import api_router

logging.config.dictConfig(log_config.dict())
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router, prefix=settings.API_V1_ENDPOINT)


@app.get("/health/")
def health():
    return {"message": "Happily serving :)"}
