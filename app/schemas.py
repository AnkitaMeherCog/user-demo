from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class ExternalPostBase(BaseModel):
    title: str
    body: str
    userId: Optional[int] = None


class ExternalPostCreate(ExternalPostBase):
    pass


class ExternalPost(ExternalPostBase):
    id: int
