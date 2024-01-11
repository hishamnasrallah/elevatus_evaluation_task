from enum import Enum
from pydantic import BaseModel, Field, EmailStr
from typing import List

candidate_collection = "candidates"


class Gender(str, Enum):
    MALE = 'male'
    FEMALE = 'female'
    NOT_SPECIFIED = 'not specified'


class CandidateModel(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    uuid: str = Field(...)
    career_level: str = Field(...)
    job_major: str = Field(...)
    years_of_experience: int = Field(...)
    degree_type: str = Field(...)
    skills: List[str] = Field(...)
    nationality: str = Field(...)
    city: str = Field(...)
    salary: float = Field(...)
    gender: Gender = Field(...)
