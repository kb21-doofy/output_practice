import React, { useState, useEffect } from 'react';
import { Book } from '../types/Book';
import { bookAPI } from '../services/api';
import BookCard from './BookCard';
import './BookList.css';

interface BookListProps {
  onEditBook: (book: Book) => void;
  refreshTrigger: number;
}

const BookList: React.FC<BookListProps> = ({ onEditBook, refreshTrigger }) => {
  const [books, setBooks] = useState<Book[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [searchQuery, setSearchQuery] = useState('');

  const fetchBooks = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await bookAPI.getBooks();
      setBooks(data);
    } catch (err) {
      setError('本の取得に失敗しました');
      console.error('Error fetching books:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async () => {
    if (!searchQuery.trim()) {
      fetchBooks();
      return;
    }

    try {
      setLoading(true);
      setError(null);
      const data = await bookAPI.searchBooks(searchQuery);
      setBooks(data);
    } catch (err) {
      setError('検索に失敗しました');
      console.error('Error searching books:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id: number) => {
    if (!window.confirm('この本を削除しますか？')) {
      return;
    }

    try {
      await bookAPI.deleteBook(id);
      setBooks(books.filter(book => book.id !== id));
    } catch (err) {
      setError('削除に失敗しました');
      console.error('Error deleting book:', err);
    }
  };

  useEffect(() => {
    fetchBooks();
  }, [refreshTrigger]);

  if (loading) {
    return <div className="loading">読み込み中...</div>;
  }

  if (error) {
    return (
      <div className="error">
        <p>{error}</p>
        <button onClick={fetchBooks}>再試行</button>
      </div>
    );
  }

  return (
    <div className="book-list">
      <div className="search-section">
        <div className="search-bar">
          <input
            type="text"
            placeholder="タイトルまたは著者で検索..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
          />
          <button onClick={handleSearch}>検索</button>
          <button onClick={() => { setSearchQuery(''); fetchBooks(); }}>
            クリア
          </button>
        </div>
      </div>

      <div className="books-grid">
        {books.length === 0 ? (
          <p className="no-books">本が見つかりませんでした</p>
        ) : (
          books.map(book => (
            <BookCard
              key={book.id}
              book={book}
              onEdit={() => onEditBook(book)}
              onDelete={() => handleDelete(book.id)}
            />
          ))
        )}
      </div>
    </div>
  );
};

export default BookList;