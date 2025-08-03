# app/domain/book_service.py
from typing import List, Optional
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from .book import Book

class BookService:
    """本に関するデータベース操作をまとめたサービスクラス"""
    
    def __init__(self, db: Session):
        self.db = db
    
    # CREATE - 本を作成
    def create_book(self, title: str, author: str, isbn: str = None, 
                   description: str = None, pages: int = None, 
                   published_year: int = None) -> Book:
        """新しい本を作成"""
        book = Book(
            title=title,
            author=author,
            isbn=isbn,
            description=description,
            pages=pages,
            published_year=published_year
        )
        self.db.add(book)        # セッションに追加
        self.db.commit()         # データベースに保存
        self.db.refresh(book)    # 作成されたIDなどを取得
        return book
    
    # READ - 本を読み取り
    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        """IDで本を取得"""
        return self.db.query(Book).filter(Book.id == book_id).first()
    
    def get_book_by_isbn(self, isbn: str) -> Optional[Book]:
        """ISBNで本を取得"""
        return self.db.query(Book).filter(Book.isbn == isbn).first()
    
    def get_books_by_author(self, author: str) -> List[Book]:
        """著者で本を検索"""
        return self.db.query(Book).filter(Book.author.ilike(f"%{author}%")).all()
    
    def get_all_books(self, skip: int = 0, limit: int = 100) -> List[Book]:
        """全ての本を取得（ページング付き）"""
        return self.db.query(Book).offset(skip).limit(limit).all()
    
    # UPDATE - 本を更新
    def update_book(self, book_id: int, **kwargs) -> Optional[Book]:
        """本の情報を更新"""
        book = self.get_book_by_id(book_id)
        if not book:
            return None
        
        # 渡された項目のみ更新
        for key, value in kwargs.items():
            if hasattr(book, key):
                setattr(book, key, value)
        
        self.db.commit()
        self.db.refresh(book)
        return book
    
    # DELETE - 本を削除
    def delete_book(self, book_id: int) -> bool:
        """本を削除"""
        book = self.get_book_by_id(book_id)
        if not book:
            return False
        
        self.db.delete(book)
        self.db.commit()
        return True
    
    # その他の便利メソッド
    def search_books(self, query: str) -> List[Book]:
        """タイトルまたは著者で本を検索"""
        return self.db.query(Book).filter(
            (Book.title.ilike(f"%{query}%")) | 
            (Book.author.ilike(f"%{query}%"))
        ).all()
    
    def get_available_books(self) -> List[Book]:
        """利用可能な本のみ取得"""
        return self.db.query(Book).filter(Book.is_available == True).all()
    
    # 貸し出し・返却機能
    def borrow_book(self, book_id: int) -> Optional[Book]:
        """本を貸し出し（1週間）"""
        book = self.get_book_by_id(book_id)
        if not book:
            return None
        
        # 既に貸し出し中の場合はエラー
        if not book.is_available:
            return None
        
        # 1週間後の日付を設定
        borrowed_until = datetime.now() + timedelta(weeks=1)
        
        book.is_available = False
        book.borrowed_until = borrowed_until
        
        self.db.commit()
        self.db.refresh(book)
        return book
    
    def return_book(self, book_id: int) -> Optional[Book]:
        """本を返却"""
        book = self.get_book_by_id(book_id)
        if not book:
            return None
        
        book.is_available = True
        book.borrowed_until = None
        
        self.db.commit()
        self.db.refresh(book)
        return book