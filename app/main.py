# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from api.book import book  
from api.user import user
from api import auth

app = FastAPI()

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174"],  # フロントエンドのURL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book.router, prefix="/api/books")
app.include_router(user.router, prefix="/api/users")
app.include_router(auth.router, prefix="/api/auth") 

# 静的ファイルの設定
app.mount("/static", StaticFiles(directory="static"), name="static")

# favicon.icoのエンドポイント
@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/favicon.ico")

@app.get("/")
def root():
    return {"message": "FastAPI is working!"}