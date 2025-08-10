from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Docker環境でのデータベース接続設定
# コンテナ間通信では、PostgreSQLコンテナのサービス名（db）とコンテナ内ポート（5432）を使用
DB_HOST = os.getenv('DB_HOST', 'db')  # Docker環境ではサービス名'db'を使用
DB_PORT = os.getenv('DB_PORT', '5432')  # コンテナ内ポート5432を使用
DB_USER = os.getenv('DB_USER', 'appuser')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME', 'booklog')

# 接続URLを組み立てる
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

print(f" データベース接続URL: postgresql://{DB_USER}:***@{DB_HOST}:{DB_PORT}/{DB_NAME}")

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# FastAPI依存注入用
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()