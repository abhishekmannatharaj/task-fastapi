from fastapi import APIRouter, HTTPException, Response, status
from db.database import connection, cursor
from api.v1.posts.schemas import PostCreate

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/")
async def read_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"data": posts}

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_posts(post: PostCreate):
    cursor.execute(
        """
        INSERT INTO posts (title, content, published)
        VALUES (%s, %s, %s)
        RETURNING *
        """,
        (post.title, post.content, post.published),
    )
    created_post = cursor.fetchone()
    connection.commit()
    return {"data": created_post}

@router.get("/latest")
async def get_latest_post():
    cursor.execute("SELECT * FROM posts ORDER BY id DESC LIMIT 1")
    post = cursor.fetchone()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No posts found"
        )
    return {"latest_post": post}

@router.get("/{id}")
async def get_post(id: int, response: Response):
    cursor.execute("SELECT * FROM posts WHERE id = %s", (id,))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )
    return {"post_detail": post}