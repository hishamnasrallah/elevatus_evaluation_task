from fastapi import APIRouter, Body, Request, status
from app.api.repositories.user import login
from app.api.v1.serializers.user import UserResponseSerializer, UserRegistrationSerializer
from core.constants.response_messages import ResponseConstants
from utils.http_response import http_response
from app.api.repositories import user

router = APIRouter(
    prefix='/v1',
    tags=[]
)


@router.post("/register/", response_model=UserResponseSerializer)
def create_user(request: Request, request_body: UserRegistrationSerializer = Body(...)):
    data = user.create_user(request_body, request)
    print(data)
    return http_response(data=data, status=status.HTTP_201_CREATED,
                         message=ResponseConstants.CREATED_MSG)


@router.post("/token")
def generate_token(email: str, password: str, request: Request):
    return login(request, email, password)
