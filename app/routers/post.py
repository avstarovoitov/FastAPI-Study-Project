from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy import func
from sqlalchemy.orm import Session

from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)


@router.get("/", response_model=list[schemas.PostOut])
async def get_posts(db: Session = Depends(get_db)):

    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).all()

    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return posts


@router.get("/{id}", response_model=schemas.PostOut)
async def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(
        models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return post


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
async def create_posts(post: schemas.PostCreate,
                       db: Session = Depends(get_db),
                       current_user: int = Depends(oauth2.get_current_user)
                       ):
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user=Depends(oauth2.get_current_user)):
    query_post = db.query(models.Post).filter(models.Post.id == id)
    post = query_post.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if post.owner_id != int(current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='No permitted')

    query_post.delete(synchronize_session=False)
    db.commit()


@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db),
                current_user=Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if post.owner_id != int(current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not permitted')

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
