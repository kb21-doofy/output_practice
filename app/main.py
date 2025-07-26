# app/main.py
from fastapi import FastAPI
from api.book import book  
from api.user import user  

app = FastAPI()
app.include_router(book.router, prefix="/api/books")
app.include_router(user.router, prefix="/api/users") 

@app.get("/")
def root():
    return {"message": "FastAPI is working!"}