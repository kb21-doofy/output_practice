import React from 'react';
import type { Book } from '../types/Book';
import './BookCard.css';

interface BookCardProps {
  book: Book;
  onEdit: () => void;
  onDelete: () => void;
  onBorrow?: (bookId: number) => void;
  onReturn?: (bookId: number) => void;
}

const BookCard: React.FC<BookCardProps> = ({ book, onEdit, onDelete, onBorrow, onReturn }) => {
  // 貸し出し期限をチェックして、期限切れの場合は自動的に利用可能にする
  const isOverdue = book.borrowed_until && new Date(book.borrowed_until) < new Date();
  const actuallyAvailable = book.is_available || isOverdue;
  
  const handleStatusClick = () => {
    if (actuallyAvailable && onBorrow) {
      onBorrow(book.id);
    } else if (!actuallyAvailable && onReturn) {
      onReturn(book.id);
    }
  };
  
  const getStatusText = () => {
    if (actuallyAvailable) {
      return '利用可能';
    } else if (book.borrowed_until) {
      const returnDate = new Date(book.borrowed_until).toLocaleDateString('ja-JP');
      return `貸出中 (返却予定: ${returnDate})`;
    } else {
      return '貸出中';
    }
  };
  return (
    <div className="book-card">
      <div className="book-header">
        <h3 className="book-title">{book.title}</h3>
        <div className="book-actions">
          <button className="edit-btn" onClick={onEdit} title="編集">
            ✏️
          </button>
          <button className="delete-btn" onClick={onDelete} title="削除">
            🗑️
          </button>
        </div>
      </div>
      
      <div className="book-info">
        <p><strong>著者:</strong> {book.author}</p>
        {book.isbn && <p><strong>ISBN:</strong> {book.isbn}</p>}
        {book.pages && <p><strong>ページ数:</strong> {book.pages}ページ</p>}
        {book.published_year && <p><strong>出版年:</strong> {book.published_year}年</p>}
        <p>
          <strong>ステータス:</strong> 
          <span 
            className={`availability ${actuallyAvailable ? 'available' : 'unavailable'} clickable`}
            onClick={handleStatusClick}
            title={actuallyAvailable ? 'クリックして貸し出し' : 'クリックして返却'}
          >
            {getStatusText()}
          </span>
        </p>
        {book.description && (
          <p className="book-description">
            <strong>説明:</strong> {book.description}
          </p>
        )}
      </div>
      
      <div className="book-footer">
        <span className="created-date">
          作成日: {new Date(book.created_at).toLocaleDateString('ja-JP')}
        </span>
      </div>
    </div>
  );
};

export default BookCard;