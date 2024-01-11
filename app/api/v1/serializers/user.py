from typing import List
from pydantic import EmailStr
from core.serializers.base import BaseModel
from core.serializers.response import BaseResponse


class UserBasicSerializer(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    # uuid: str


class UserRegistrationSerializer(UserBasicSerializer):
    password: str


class UserResponseSerializer(BaseResponse):
    data: List[UserBasicSerializer]
