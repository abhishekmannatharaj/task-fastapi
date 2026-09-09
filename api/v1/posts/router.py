from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from api.v1.auth.security import get_current_user
from db.models import User
from db.database import get_db
from db.models import Post
from api.v1.posts.schemas import PostCreate, PostResponse

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get("/", response_model=List[PostResponse])
async def read_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
async def create_posts(
    post: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Create new Post instance using validated data
    new_post = Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/latest", response_model=PostResponse)
async def get_latest_post(db: Session = Depends(get_db)):
    post = db.query(Post).order_by(Post.id.desc()).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No posts found"
        )
    return post


@router.get("/{id}", response_model=PostResponse)
async def get_post(id: int, response: Response, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )
    return post