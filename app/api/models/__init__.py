from app.api.models.user import *
from app.api.models.candidates import *

"""
Any model need to be add to the __all__ variable to be readable for alembic
and no need to modify env.py in alembic folder
"""

__all__ = ("User", "CandidateModel",)
del globals()["BaseModel"]
