import logging

import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from app.api.v1.routers import api_router
from core.settings.base import settings

logger = logging.getLogger(__name__)
logger.level = logging.INFO
logger.info("echoing something from the uicheckapp logger")

app = FastAPI(title="Elevatus", docs_url="/elevatus/docs",
              openapi_url="/elevatus/openapi.json")


# CORS
origins = ["*"]

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)
app.mongodb_client = MongoClient(settings.db_url)
app.database = app.mongodb_client[settings.db_name]

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Elevatus Evaluation Task",
        version="1.0.0",
        description="The documentation of candidates service",
        routes=app.routes,
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run(app)
