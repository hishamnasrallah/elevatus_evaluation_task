from app.api.v1.views.health_check import router as beat_router
from app.api.v1.views.user import router as user_router
from app.api.v1.views.candidates import router as candidate_router

__all__ = ("beat_router", "user_router", "candidate_router")
