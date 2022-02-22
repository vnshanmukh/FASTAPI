import models,schemas
from fastapi import Depends, FastAPI,Response,HTTPException,status, APIRouter
from sqlalchemy.orm import Session
import database,oauth
from typing import List

router = APIRouter(
    prefix="/posts",
    tags=['posts']
)

@router.get('/', response_model= List[schemas.Post])
async def get_all(db: Session = Depends(database.get_db)):
    posts = db.query(models.Post).all()
    return posts

@router.post('/', response_model= schemas.Post)
async def create_post(post:schemas.PostCreate,db: Session = Depends(database.get_db),get_current_user : str  = Depends(oauth.get_current_user)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/{id}", response_model=schemas.Post)
async def get_post(id:int,db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with {id} not found")
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:int,db: Session = Depends(database.get_db),get_current_user : str  = Depends(oauth.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
    post.delete(synchronize_session = False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model= schemas.Post)
async def update_post(id:int, updated_post:schemas.PostCreate,db: Session = Depends(database.get_db),get_current_user : str  = Depends(oauth.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()