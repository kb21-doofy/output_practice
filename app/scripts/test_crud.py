# test_crud.py - CRUD操作のテストスクリプト
from app.infrastructure.db import get_db
from app.domain.book_service import BookService

def test_crud_operations():
    """CRUD操作を順番にテストする"""
    
    # データベースセッション取得
    db = next(get_db())
    book_service = BookService(db)
    
    print("📚 CRUD操作テスト開始！\n")
    
    # =========================
    # CREATE - 本を作成
    # =========================
    print("🔨 1. CREATE - 本を作成")
    book1 = book_service.create_book(
        title="Python入門",
        author="山田太郎",
        isbn="978-4-12345-678-9",
        description="Pythonの基礎から応用まで学べる本です",
        pages=300,
        published_year=2023
    )
    print(f"   作成された本: {book1}")
    
    book2 = book_service.create_book(
        title="FastAPI実践ガイド", 
        author="佐藤花子",
        isbn="978-4-98765-432-1",
        pages=250,
        published_year=2024
    )
    print(f"   作成された本: {book2}")
    print()
    
    # =========================
    # READ - 本を読み取り
    # =========================
    print("📖 2. READ - 本を読み取り")
    
    # IDで取得
    found_book = book_service.get_book_by_id(book1.id)
    print(f"   ID {book1.id} の本: {found_book.title}")
    
    # ISBNで取得
    found_by_isbn = book_service.get_book_by_isbn("978-4-98765-432-1")
    print(f"   ISBN検索: {found_by_isbn.title}")
    
    # 著者で検索
    books_by_author = book_service.get_books_by_author("山田")
    print(f"   '山田'を含む著者の本: {len(books_by_author)}冊")
    
    # 全件取得
    all_books = book_service.get_all_books()
    print(f"   全ての本: {len(all_books)}冊")
    print()
    
    # =========================
    # UPDATE - 本を更新
    # =========================
    print("✏️  3. UPDATE - 本を更新")
    updated_book = book_service.update_book(
        book1.id,
        title="Python完全マスター（改訂版）",
        pages=350
    )
    print(f"   更新後: {updated_book.title} ({updated_book.pages}ページ)")
    print()
    
    # =========================
    # 検索機能テスト
    # =========================
    print("🔍 4. 検索機能テスト")
    search_results = book_service.search_books("Python")
    print(f"   'Python'で検索: {len(search_results)}冊見つかりました")
    for book in search_results:
        print(f"     - {book.title}")
    print()
    
    # =========================
    # DELETE - 本を削除
    # =========================
    print("🗑️  5. DELETE - 本を削除")
    deleted = book_service.delete_book(book2.id)
    print(f"   削除結果: {'成功' if deleted else '失敗'}")
    
    # 削除確認
    remaining_books = book_service.get_all_books()
    print(f"   残りの本: {len(remaining_books)}冊")
    print()
    
    print("✅ CRUD操作テスト完了！")
    
    # セッションクローズ
    db.close()

if __name__ == "__main__":
    test_crud_operations()