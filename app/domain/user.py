# app/domain/user.py
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)    # メールアドレス（必須・一意）
    name = Column(String(100), nullable=False)                              # 表示名（必須）
    hashed_password = Column(String(255), nullable=False)                   # ハッシュ化されたパスワード（必須）
    
    def __repr__(self):
        return f"<User(id={self.id},', email='{self.email}', name='{self.name}')>"
