
from datetime import datetime
import email
from turtle import title
from pydantic import BaseModel, EmailStr, Field

class PostBase(BaseModel):
    title:str
    content :str
    published: bool = Field(True)

class PostCreate(PostBase):
    pass

class Post(BaseModel):
    id : int
    created_at: datetime
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email : EmailStr
    password : str

class UserOut(BaseModel):
    email : EmailStr
    created_at: datetime
    class Config:
        orm_mode = True