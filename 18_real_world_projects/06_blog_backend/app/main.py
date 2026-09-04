"""
Blog Backend API Main Entrypoint.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from app.database import Base, SessionLocal, engine
from app.models import BlogPost

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Blog Backend API")


class PostCreate(BaseModel):
    title: str
    slug: str
    body: str


class PostOut(BaseModel):
    id: int
    title: str
    slug: str
    body: str


@app.post("/posts/", response_model=PostOut, status_code=201)

def create_post(payload: PostCreate) -> PostOut:
    with SessionLocal() as db:
        post = BlogPost(title=payload.title, slug=payload.slug, body=payload.body)
        db.add(post)
        db.commit()
        db.refresh(post)
        return PostOut(id=post.id, title=post.title, slug=post.slug, body=post.body)


@app.get("/posts/{slug}", response_model=PostOut)

def get_post_by_slug(slug: str) -> PostOut:
    with SessionLocal() as db:
        stmt = select(BlogPost).where(BlogPost.slug == slug)
        post = db.scalars(stmt).first()
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        return PostOut(id=post.id, title=post.title, slug=post.slug, body=post.body)
