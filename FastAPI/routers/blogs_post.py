from fastapi import APIRouter, status , Query
from enum import Enum
from typing import Optional
from pydantic import BaseModel

router = APIRouter(prefix='/blog', tags=['blog'])


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'blog': blog,
        'version': version
    }


@router.post('/new/{id_blog}/comment')
def new_comment(blog: BlogModel, id_blog: int,
                comment_id: int = Query(None,
                                        title='ID of the comment',
                                        description="Description of the comment ID")
                ):
    return {
        'blog': blog,
        'id': id_blog,
        'comment_id': comment_id
    }

