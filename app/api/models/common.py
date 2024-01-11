from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime
from typing import Optional

class BaseMongoModel(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        json_encoders = {
            ObjectId: str
        }
        allow_population_by_field_name = True
        arbitrary_types_allowed = True