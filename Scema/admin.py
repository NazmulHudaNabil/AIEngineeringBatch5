import datetime
import pydantic


class Admin(pydantic.BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True