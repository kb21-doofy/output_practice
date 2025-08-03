# app/domain/book.py
from sqlalchemy import Column, String, Text, Integer, Boolean, DateTime
from core.database import BaseModel

class Book(BaseModel):
    """本のモデル"""
    __tablename__ = "books"  # テーブル名を指定
    
    # 基本情報
    title = Column(String(200), nullable=False, index=True)  # タイトル（必須、インデックス付き）
    author = Column(String(100), nullable=False)            # 著者（必須）
    isbn = Column(String(17), unique=True, index=True)      # ISBN（一意、インデックス付き）
    
    # 詳細情報
    description = Column(Text)                              # 説明（長いテキスト）
    pages = Column(Integer)                                 # ページ数
    published_year = Column(Integer)                        # 出版年
    
    # ステータス
    is_available = Column(Boolean, default=True)            # 利用可能かどうか
    borrowed_until = Column(DateTime, nullable=True)        # 貸し出し期限
    
    def __repr__(self):
        """オブジェクトの文字列表現"""
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}')>"