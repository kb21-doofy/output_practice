import React from 'react';
import { Book } from '../types/Book';
import './BookCard.css';

interface BookCardProps {
  book: Book;
  onEdit: () => void;
  onDelete: () => void;
}

const BookCard: React.FC<BookCardProps> = ({ book, onEdit, onDelete }) => {
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
        {book.description && (
          <p className="book-description">
            <strong>説明:</strong> {book.description}
          </p>
        )}
      </div>
      
      <div className="book-footer">
        <span className={`availability ${book.is_available ? 'available' : 'unavailable'}`}>
          {book.is_available ? '利用可能' : '貸出中'}
        </span>
        <span className="created-date">
          作成日: {new Date(book.created_at).toLocaleDateString('ja-JP')}
        </span>
      </div>
    </div>
  );
};

export default BookCard;