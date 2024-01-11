from core.constants.service import Service


class ServiceUnavailable(Exception):

    def __init__(self, message=Service.NOT_AVAILABLE):
        self.message = message
        self.status = 400
        super().__init__(self.message, self.status)


class NotAcceptable(Exception):

    def __init__(self, message=Service.NOT_ACCESSIBLE):
        self.message = message
        self.status = 400
        super().__init__(self.message, self.status)
