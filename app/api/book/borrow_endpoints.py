# 貸し出し・返却エンドポイントを追加するためのコード
# このコードをbook.pyの最後に追加してください

@router.post("/{book_id}/borrow", response_model=dict)
def borrow_book(book_id: int, db: Session = Depends(get_db)):
    """本を貸し出し（1週間）"""
    book_service = BookService(db)
    book = book_service.borrow_book(book_id)
    
    if not book:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Book not found or not available")
    
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

@router.post("/{book_id}/return", response_model=dict)
def return_book(book_id: int, db: Session = Depends(get_db)):
    """本を返却"""
    book_service = BookService(db)
    book = book_service.return_book(book_id)
    
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
