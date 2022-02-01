from http.client import HTTPException
from fastapi import Depends, FastAPI,Response,HTTPException,status

import database
from sqlalchemy.orm import Session
import models,schemas

models.database.Base.metadata.create_all(bind=database.engine)
app = FastAPI()



@app.get('/posts')
async def Job(db: Session = Depends(database.get_db)):
    posts = db.query(models.Post).all()
    return posts

@app.post('/posts')
async def create_post(post:schemas.PostBase,db: Session = Depends(database.get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.get("/posts/{id}")
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

@app.put("/posts/{id}")
async def update_post(id:int, updated_post:schemas.PostBase,db: Session = Depends(database.get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()