from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

class PostBase(BaseModel):
    title:str
    content :str
    published: bool = Field(True)

class PostCreate(PostBase):
    pass

class Post(BaseModel):
    id : int
    title: str
    content: str
    created_at: datetime
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email : EmailStr
    password : str

class UserOut(BaseModel):
    id : int
    email : EmailStr
    created_at: datetime
    class Config:
        orm_mode = True