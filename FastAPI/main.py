from fastapi import FastAPI
from routers import blogs_get, blogs_post, user
from db import model
from db.database import engine
from auth import authentication


app = FastAPI()
app.include_router(authentication.router)
app.include_router(blogs_get.router)
app.include_router(blogs_post.router)
app.include_router(user.router)

@app.get('/')
def index():
    return "This is the first page"


model.Base.metadata.create_all(engine)

