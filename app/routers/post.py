import models,schemas,database,oauth
from fastapi import Depends,Response,HTTPException,status, APIRouter
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/posts",
    tags=['posts']
)

@router.get('/', response_model= List[schemas.Post])
async def get_all(db: Session = Depends(database.get_db),current_user : int  = Depends(oauth.get_current_user)):
    posts = db.query(models.Post).all()
    return posts

@router.post('/', response_model= schemas.Post)
async def create_post(post:schemas.PostCreate,db: Session = Depends(database.get_db),current_user : int  = Depends(oauth.get_current_user)):
    new_post = models.Post(owner_id = current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/{id}", response_model=schemas.Post)
async def get_post(id:int,db: Session = Depends(database.get_db),current_user : int  = Depends(oauth.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with {id} not found")
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    print(type(post.owner_id),type(current_user.id))
    if post.owner_id == int(current_user.id):
        post_query.delete(synchronize_session=False)
        db.commit()
    
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model= schemas.Post)
async def update_post(id:int, updated_post:schemas.PostCreate,db: Session = Depends(database.get_db),current_user : int = Depends(oauth.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {id} not found")
    if post.owner_id != int(current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Not authorized to perform requested action")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()

