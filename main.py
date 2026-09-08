from fastapi import FastAPI
from db.database import engine, Base
import db.models  # Ensures the Post model is registered with Base before table creation
from api.v1.posts.router import router as posts_router

# Auto-create tables in PostgreSQL if they don't already exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Instagram-Style Backend API",
    version="1.0.0",
    description="Modular CRUD backend using FastAPI and PostgreSQL",
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Server is up and running"}

# Register modular routers under versioned path prefix
app.include_router(posts_router, prefix="/api/v1")