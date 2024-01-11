from fastapi import APIRouter
from app.api.v1.views import beat_router, user_router, candidate_router

api_router = APIRouter()
api_router.include_router(user_router, tags=["user"], prefix="/user")
api_router.include_router(candidate_router, tags=["candidate"], prefix="/candidate")
api_router.include_router(beat_router, tags=["beat"])
