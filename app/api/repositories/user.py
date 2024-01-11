import uuid
from passlib.context import CryptContext
from app.api.models.user import User
from fastapi import HTTPException, status
from core.exceptions.user import UserAlreadyExists
from utils.tokens import create_access_token, pwd_context


def create_user(request_body, request):
    request_dict = request_body.dict()

    existing_user = request.app.database["users"].find_one({
        "email": request_dict["email"]
    })
    if existing_user:
        raise UserAlreadyExists

    new_uuid = uuid.uuid4()
    uuid_str = str(new_uuid)
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_password = pwd_context.hash(request_dict["password"])
    request_dict["password"] = hashed_password
    request_dict["uuid"] = uuid_str
    new_rec = request.app.database["users"].insert_one(request_dict)
    created_item = request.app.database["users"].find_one({
        "_id": new_rec.inserted_id
    })

    if new_rec.inserted_id:
        created_item['_id'] = str(new_rec.inserted_id)
        del created_item['password']
        return created_item  # Return the inserted user data
    else:
        raise HTTPException(status_code=500, detail="Failed to insert user into the database")


def authenticate_user(request, email: str, password: str):
    user = request.app.database["users"].find_one({"email": email})
    if not user or not pwd_context.verify(password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        print(user["first_name"])
    return User(**user)


def login(request, email: str, password: str):
    user = authenticate_user(request, email, password)
    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
