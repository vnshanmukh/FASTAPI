from http.client import HTTPException
from typing import List
from unittest import async_case
from fastapi import Depends, FastAPI,Response,HTTPException,status
from database import get_db

import database
from sqlalchemy.orm import Session
import models,schemas

models.database.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

@app.get('/posts', response_model= List[schemas.Post])
async def get_all(db: Session = Depends(database.get_db)):
    posts = db.query(models.Post).all()
    return posts

@app.post('/posts', response_model= schemas.Post)
async def create_post(post:schemas.PostCreate,db: Session = Depends(database.get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.get("/posts/{id}", response_model=schemas.Post)
async def get_post(id:int,db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with {id} not found")
    return post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
    post.delete(synchronize_session = False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}", response_model= schemas.Post)
async def update_post(id:int, updated_post:schemas.PostCreate,db: Session = Depends(database.get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()

@app.post("/user", response_model=schemas.UserOut)
async def create_user(user:schemas.UserCreate,db: Session = Depends(database.get_db)):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
