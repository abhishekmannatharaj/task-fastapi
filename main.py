from fastapi import FastAPI
from api.v1.posts.router import router as posts_router

app = FastAPI(title="Instagram Clone API")

# Register versioned routes
app.include_router(posts_router, prefix="/api/v1")

@app.get("/")
async def read_root():
    return {"message": "Server is running"}