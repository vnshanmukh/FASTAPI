from http.client import HTTPException
from fastapi import FastAPI,Response,HTTPException,status
from pydantic import BaseModel, Field

app = FastAPI()

Posts = [
    {
        "id" : 1,
        "Title":"SDE",
        "Author": "Goo",
        "Description":"Need ndjsm "
    },
    {
        "id" : 2,
        "Title":"SDE",
        "Author": "Goo",
        "Description":"Need ndjsm "
    }
]

def find_post(id):
    for i in Posts:
        if i["id"] == id:
            return i

def find_index_post(id):
    for i,val in enumerate(Posts):
        if val["id"] == id:
            return i

class Post(BaseModel):
    Title : str = Field(...)
    Author : str = Field(...)
    Description :str = Field(...)

@app.get('/posts')
async def Job():
    return Posts

@app.post('/posts/{id}' , response_model= Post)
async def create_post(post:Post, id:int):
    post_dict = post.dict()
    post_dict["id"] = id
    Posts.append(post_dict)
    return post

@app.get("/posts/{id}")
async def get_post(id:int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with {id} not found")
    return post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
    Posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
async def update_post(id:int, post:Post):
    index = find_index_post(id)
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
    post_dict = post.dict()
    post_dict["id"] = id
    Posts[index] = post_dict
    return {"new_data" : post_dict}

