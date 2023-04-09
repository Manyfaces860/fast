from sqlalchemy.orm import session
import  schemas
from fastapi import FastAPI , Response, status, HTTPException, Depends , APIRouter
import model
from database import engine, get_db
import oauth2

router = APIRouter()

@router.post("/post", status_code=status.HTTP_201_CREATED )
def posting(post: schemas.PostCreate, db: session = Depends(get_db) , user_id: int = Depends(oauth2.get_current_user)):
    new_post = model.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"post": new_post}

@router.get("/post/{id}", status_code=status.HTTP_302_FOUND)
def get_posts(id: int, db: session = Depends(get_db)):
    post = db.query(model.Post).filter(model.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="the post you are looking for is not here")
    return {"post": post} 

@router.post("/post/{id}", status_code=status.HTTP_201_CREATED)
def update_posts(updated_post: schemas.PostCreate, id : int,db: session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    post = db.query(model.Post).filter(model.Post.id == id)
    
    if post.first() == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND , detail= "the post you are looking for is not here")
    
    post.update(updated_post.dict(), synchronize_session= False)
    db.commit()
    
    return {"post": post.first()}

@router.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts( id : int ,db: session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    post = db.query(model.Post).filter(model.Post.id == id)
    
    if post.first() == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="the post you are looking for is not here")
    
    post.delete(synchronize_session= False)
    db.commit()
    
    return Response(status_code= status.HTTP_204_NO_CONTENT)

