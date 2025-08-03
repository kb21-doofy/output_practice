import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from infrastructure.db import get_db
from domain.book_service import BookService
from domain.book import Book

# Pydanticモデル
class BookCreate(BaseModel):
    title: str
    author: str
    isbn: Optional[str] = None
    description: Optional[str] = None
    pages: Optional[int] = None
    published_year: Optional[int] = None

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    description: Optional[str] = None
    pages: Optional[int] = None
    published_year: Optional[int] = None

router = APIRouter()

@router.get("/", response_model=List[dict])
def get_books(db: Session = Depends(get_db)):
    book_service = BookService(db)
    books = book_service.get_all_books()
    
    # Bookオブジェクトを辞書に変換
    books_data = []
    for book in books:
        books_data.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "isbn": book.isbn,
            "description": book.description,
            "pages": book.pages,
            "published_year": book.published_year,
            "is_available": book.is_available,
            "created_at": book.created_at.isoformat() if book.created_at else None,
            "updated_at": book.updated_at.isoformat() if book.updated_at else None,
        })
    
    return books_data

@router.post("/", response_model=dict)
def create_book(book_data: BookCreate, db: Session = Depends(get_db)):
    book_service = BookService(db)
    book = book_service.create_book(
        title=book_data.title,
        author=book_data.author,
        isbn=book_data.isbn,
        description=book_data.description,
        pages=book_data.pages,
        published_year=book_data.published_year
    )
    
    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "isbn": book.isbn,
        "description": book.description,
        "pages": book.pages,
        "published_year": book.published_year,
        "is_available": book.is_available,
        "borrowed_until": book.borrowed_until.isoformat() if book.borrowed_until else None,
        "created_at": book.created_at.isoformat() if book.created_at else None,
        "updated_at": book.updated_at.isoformat() if book.updated_at else None,
    }

@router.get("/{book_id}", response_model=dict)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book_service = BookService(db)
    book = book_service.get_book_by_id(book_id)
    
    if not book:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Book not found")
    
    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "isbn": book.isbn,
        "description": book.description,
        "pages": book.pages,
        "published_year": book.published_year,
        "is_available": book.is_available,
        "borrowed_until": book.borrowed_until.isoformat() if book.borrowed_until else None,
        "created_at": book.created_at.isoformat() if book.created_at else None,
        "updated_at": book.updated_at.isoformat() if book.updated_at else None,
    }

@router.put("/{book_id}", response_model=dict)
def update_book(book_id: int, book_data: BookUpdate, db: Session = Depends(get_db)):
    book_service = BookService(db)
    
    # 更新データを準備
    update_data = {}
    if book_data.title is not None:
        update_data["title"] = book_data.title
    if book_data.author is not None:
        update_data["author"] = book_data.author
    if book_data.isbn is not None:
        update_data["isbn"] = book_data.isbn
    if book_data.description is not None:
        update_data["description"] = book_data.description
    if book_data.pages is not None:
        update_data["pages"] = book_data.pages
    if book_data.published_year is not None:
        update_data["published_year"] = book_data.published_year
    
    book = book_service.update_book(book_id, **update_data)
    
    if not book:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Book not found")
    
    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "isbn": book.isbn,
        "description": book.description,
        "pages": book.pages,
        "published_year": book.published_year,
        "is_available": book.is_available,
        "borrowed_until": book.borrowed_until.isoformat() if book.borrowed_until else None,
        "created_at": book.created_at.isoformat() if book.created_at else None,
        "updated_at": book.updated_at.isoformat() if book.updated_at else None,
    }

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_service = BookService(db)
    success = book_service.delete_book(book_id)
    
    if not success:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Book not found")
    
    return {"message": "Book deleted successfully"}

@router.get("/search", response_model=List[dict])
def search_books(q: str, db: Session = Depends(get_db)):
    book_service = BookService(db)
    books = book_service.search_books(q)
    
    books_data = []
    for book in books:
        books_data.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "isbn": book.isbn,
            "description": book.description,
            "pages": book.pages,
            "published_year": book.published_year,
            "is_available": book.is_available,
            "created_at": book.created_at.isoformat() if book.created_at else None,
            "updated_at": book.updated_at.isoformat() if book.updated_at else None,
        })
    
    return books_data