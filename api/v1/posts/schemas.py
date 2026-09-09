from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)