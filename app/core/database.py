# app/core/database.py
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

# ベースクラス - すべてのモデルが継承する
Base = declarative_base()

class BaseModel(Base):
    """すべてのモデルの基底クラス"""
    __abstract__ = True  # このクラス自体はテーブルにしない
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())