from core.constants.user import UserConstants
from fastapi import HTTPException

class UserAlreadyExists(HTTPException):

    def __init__(self, message_key=UserConstants.EMAIL_ALREADY_EXISTS_ERROR):
        self.message_key = message_key
        self.status = 400

        super().__init__(self.status, self.message_key)