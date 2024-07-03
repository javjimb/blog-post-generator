from fastapi import FastAPI
from app.api import search, generate_blog

app = FastAPI()

app.include_router(search.router)
app.include_router(generate_blog.router)
