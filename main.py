from fastapi import FastAPI
from db.database import engine, Base
import db.models
from api.v1.posts.router import router as posts_router
from api.v1.auth.auth_router import router as auth_router

# Auto-create tables in PostgreSQL
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Instagram-Style Backend API",
    version="1.0.0",
    description="Modular CRUD backend using FastAPI, SQLAlchemy, and PostgreSQL",
)

@app.get("/")
def read_root():
    return {"message": "Server is up and running"}

app.include_router(posts_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")