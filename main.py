import time
from typing import Optional
from fastapi import FastAPI , Response , status , HTTPException
from fastapi.params import Body
import psycopg2
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

#we will give a scheme like a rules to follow
class Post(BaseModel):
    title: str 
    content: str
    published: bool = True
    rating: Optional[int] = None
while True:
    try:
        connection = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='rslogin1823?', cursor_factory=RealDictCursor) #later have to hide this
        cursor = connection.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)

mypost = [{"title": "Gladiator", "content": "thala ajith", "id": 1}, {"title": "GBU", "content": "Ak-arakan", "id": 2}]

def find_post(id):
    for p in mypost:
        if p['id'] == id:
            return p

@app.get("/")
async def read_root():
    return {"message": "World"}

@app.get("/posts")
async def read_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_posts(post: Post):
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

@app.get("/posts/latest")
async def get_latest_post():    
    cursor.execute("SELECT * FROM posts ORDER BY id DESC LIMIT 1")
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No posts found")
    return {"latest_post": post}

@app.get("/posts/{id}")
async def get_post(id: int, response: Response):
    cursor.execute("SELECT * FROM posts WHERE id = %s", (id,))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"post_detail": post}

