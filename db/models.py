from datetime import datetime
from typing import Optional
from pydantic import BaseModel


# Base schema containing shared attributes
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


# Your existing creation model (inherits all fields from PostBase)
class PostCreate(PostBase):
    pass


# Response model - defines exactly what is sent back to the client
class PostResponse(PostBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Allows Pydantic to read SQLAlchemy ORM models