import React, { useState, useEffect } from 'react';
import type { Book } from '../types/Book';
import { bookAPI } from '../services/api';
import BookCard from './BookCard';
import './BorrowedBookList.css';

const BorrowedBookList: React.FC = () => {
  const [borrowedBooks, setBorrowedBooks] = useState<Book[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchBorrowedBooks = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await bookAPI.getBorrowedBooks();
      setBorrowedBooks(data);
    } catch (err) {
      setError('貸出中の本の取得に失敗しました');
      console.error('Error fetching borrowed books:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleReturn = async (id: number) => {
    try {
      const updatedBook = await bookAPI.returnBook(id);
      // 返却された本を一覧から削除
      setBorrowedBooks(borrowedBooks.filter(book => book.id !== id));
    } catch (err) {
      setError('返却に失敗しました');
      console.error('Error returning book:', err);
    }
  };

  // 貸出期限の表示用フォーマット
  const formatBorrowedUntil = (borrowedUntil: string | null) => {
    if (!borrowedUntil) return 'なし';
    const date = new Date(borrowedUntil);
    return `${date.getFullYear()}/${(date.getMonth() + 1).toString().padStart(2, '0')}/${date.getDate().toString().padStart(2, '0')}`;
  };

  // 期限切れかどうかをチェック
  const isOverdue = (borrowedUntil: string | null) => {
    if (!borrowedUntil) return false;
    const dueDate = new Date(borrowedUntil);
    const today = new Date();
    today.setHours(0, 0, 0, 0); // 時間を00:00:00にリセット
    return dueDate < today;
  };

  useEffect(() => {
    fetchBorrowedBooks();
  }, []);

  if (loading) {
    return <div className="loading">貸出中の本を読み込み中...</div>;
  }

  if (error) {
    return (
      <div className="error">
        <p>{error}</p>
        <button onClick={fetchBorrowedBooks}>再試行</button>
      </div>
    );
  }

  return (
    <div className="borrowed-book-list">
      <div className="borrowed-header">
        <h2>📚 貸出中の本一覧</h2>
        <p>現在 {borrowedBooks.length} 冊の本が貸し出されています</p>
        <button onClick={fetchBorrowedBooks} className="refresh-button">
          🔄 更新
        </button>
      </div>

      {borrowedBooks.length === 0 ? (
        <div className="no-borrowed-books">
          <p>現在貸し出し中の本はありません</p>
        </div>
      ) : (
        <div className="borrowed-books-grid">
          {borrowedBooks.map(book => (
            <div key={book.id} className={`borrowed-book-card ${isOverdue(book.borrowed_until) ? 'overdue' : ''}`}>
              <BookCard
                book={book}
                onEdit={() => {}} // 貸出中の本は編集不可
                onDelete={() => {}} // 貸出中の本は削除不可
                onBorrow={() => {}} // 既に貸出中なので無効
                onReturn={handleReturn}
              />
              <div className="borrowed-info">
                <div className="due-date">
                  <strong>返却予定日:</strong> 
                  <span className={isOverdue(book.borrowed_until) ? 'overdue-date' : ''}>
                    {formatBorrowedUntil(book.borrowed_until)}
                  </span>
                  {isOverdue(book.borrowed_until) && (
                    <span className="overdue-label">⚠️ 期限切れ</span>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default BorrowedBookList;