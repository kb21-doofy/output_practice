# app/main.py
from fastapi import FastAPI
from app.api.v1 import book  # ルーター

app = FastAPI()
app.include_router(book.router, prefix="/api/v1/books")

@app.get("/")
def root():
    return {"message": "FastAPI is working!"}