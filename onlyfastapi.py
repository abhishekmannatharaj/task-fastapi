import time
from typing import Optional
from fastapi import FastAPI , Response , status , HTTPException
from fastapi.params import Body
import psycopg2
from pydantic import BaseModel
from random import randrange

app = FastAPI()

#we will give a scheme like a rules to follow
class Post(BaseModel):
    title: str 
    content: str
    published: bool = True
    rating: Optional[int] = None


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
    return {"data": mypost} 

@app.post("/posts")
async def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    mypost.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/latest")
async def get_latest_post():    
    post = mypost[len(mypost) - 1]
    return {"latest_post": post}

@app.get("/posts/{id}")
async def get_post(id: int, response: Response):
    post = find_post(id)   
    if not post:  
    #exception handling
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    # response. status_code = status.HTTP_404_NOT_FOUND
    # return {'message': f"post with id: {id} was not found"}
    return {"post_detail": post}

