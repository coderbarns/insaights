from dotenv import load_dotenv

load_dotenv(".env")

import logging
import logging.config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import settings, log_config
from src.api.v1.api import api_router

logging.config.dictConfig(log_config.dict())
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router, prefix=settings.API_V1_ENDPOINT)


origins = [
    "http://localhost:3000",
    "http://localhost:5000",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health/")
def health():
    return {"message": "Happily serving :)"}
