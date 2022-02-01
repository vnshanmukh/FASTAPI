
from pydantic import BaseModel, Field

class PostBase(BaseModel):
    title:str
    content :str
    published: bool = Field(True)

class PostCreate(PostBase):
    pass
