from typing import List, Optional
from pydantic import EmailStr
from app.api.models.candidates import Gender
from core.serializers.base import BaseModel
from core.serializers.response import BaseResponse


class CandidateBasicSerializer(BaseModel):
    _id: Optional[str]
    first_name: str
    last_name: str
    email: EmailStr
    career_level: str
    job_major: str
    years_of_experience: int
    degree_type: str
    skills: List[str]
    nationality: str
    city: str
    salary: float
    gender: Gender


class CandidateResponseSerializer(BaseResponse):
    data: List[CandidateBasicSerializer]
