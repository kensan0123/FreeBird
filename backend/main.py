from core.logger import logger
from fastapi import FastAPI
from routers import generate, publish

app = FastAPI()

app.include_router(generate.router)
app.include_router(publish.router)

logger.info("FastAPI application started successfully")
