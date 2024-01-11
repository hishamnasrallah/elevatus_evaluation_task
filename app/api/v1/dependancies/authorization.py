from fastapi import Security
from fastapi.security import APIKeyHeader
import jwt


def validate_authorization(
        authorization: str = Security(APIKeyHeader(name='Authorization'))):
    try:
        authorization = authorization.replace("Bearer ", "")
        decoded = jwt.decode(authorization,
                             options={"verify_signature": False})
        return decoded
    except (jwt.DecodeError, jwt.ExpiredSignatureError):
        raise "Invalid Authentication"
