from json import dumps
# from fastapi_camelcase import CamelModel
from pydantic import BaseModel

import datetime


class BaseModel(BaseModel):
    def dict(self):
        data = {k: v for k, v in self.__dict__.items() if v is not None}
        for i in data:
            if isinstance(data[i], (datetime.datetime, datetime.date)):
                data[i] = dumps(data[i], indent=4, sort_keys=True, default=str)
        return data
