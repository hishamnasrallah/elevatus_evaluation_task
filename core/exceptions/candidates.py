from core.constants.candidates import CandidateConstants
from fastapi import HTTPException


class CandidateDoesNotExist(HTTPException):

    def __init__(self, message_key=CandidateConstants.CANDIDATE_DOES_NOT_EXIST_ERROR):
        self.message_key = message_key
        self.status = 404

        super().__init__(self.status, self.message_key)


class CandidateDoesUpdated(HTTPException):
    def __init__(self,
                 message_key=CandidateConstants.CANDIDATE_DOES_NOT_UPDATED_ERROR,
                 field_name=None):
        if field_name:
            self.message_key = {field_name: message_key}
        else:
            self.message_key = message_key
        self.status = 400
        super().__init__(self.status, self.message_key)

