from fastapi import APIRouter, status
from enum import Enum

router = APIRouter(prefix='/blog', tags=['blog'])


@router.get("/all", status_code=status.HTTP_200_OK)
def get_all_blogs():
    return {f"message: Thissss all the blogs"}


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@router.get("/type/{type}")
def blog_type(type:BlogType):
    return {f"message: This is the type : {type}"}


# @router.get("/")
# def query(page, page_size):
#     return {f"page = {page} and page size = {page_size}"}


@router.get("/{id}")
def blogs(id: int):
    return {f"message: This TEST the id : {id}"}
