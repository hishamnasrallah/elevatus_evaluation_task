from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    uuid: str = Field(...)
    password: str = Field(...)
