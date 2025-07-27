import React, { useState, useEffect } from 'react';
import { Book, CreateBookRequest, UpdateBookRequest } from '../types/Book';
import { bookAPI } from '../services/api';
import './BookForm.css';

interface BookFormProps {
  book?: Book;
  onSuccess: () => void;
  onCancel: () => void;
}

const BookForm: React.FC<BookFormProps> = ({ book, onSuccess, onCancel }) => {
  const [formData, setFormData] = useState({
    title: '',
    author: '',
    isbn: '',
    description: '',
    pages: '',
    published_year: ''
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (book) {
      setFormData({
        title: book.title,
        author: book.author,
        isbn: book.isbn || '',
        description: book.description || '',
        pages: book.pages?.toString() || '',
        published_year: book.published_year?.toString() || ''
      });
    }
  }, [book]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!formData.title.trim() || !formData.author.trim()) {
      setError('タイトルと著者は必須です');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const bookData = {
        title: formData.title.trim(),
        author: formData.author.trim(),
        isbn: formData.isbn.trim() || undefined,
        description: formData.description.trim() || undefined,
        pages: formData.pages ? parseInt(formData.pages) : undefined,
        published_year: formData.published_year ? parseInt(formData.published_year) : undefined
      };

      if (book) {
        // 更新
        await bookAPI.updateBook(book.id, bookData as UpdateBookRequest);
      } else {
        // 作成
        await bookAPI.createBook(bookData as CreateBookRequest);
      }

      onSuccess();
    } catch (err: any) {
      setError(err.response?.data?.detail || '保存に失敗しました');
      console.error('Error saving book:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="book-form-overlay">
      <div className="book-form">
        <div className="form-header">
          <h2>{book ? '本を編集' : '新しい本を追加'}</h2>
          <button className="close-btn" onClick={onCancel}>×</button>
        </div>

        {error && <div className="error-message">{error}</div>}

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="title">タイトル *</label>
            <input
              type="text"
              id="title"
              name="title"
              value={formData.title}
              onChange={handleChange}
              required
              placeholder="本のタイトルを入力..."
            />
          </div>

          <div className="form-group">
            <label htmlFor="author">著者 *</label>
            <input
              type="text"
              id="author"
              name="author"
              value={formData.author}
              onChange={handleChange}
              required
              placeholder="著者名を入力..."
            />
          </div>

          <div className="form-group">
            <label htmlFor="isbn">ISBN</label>
            <input
              type="text"
              id="isbn"
              name="isbn"
              value={formData.isbn}
              onChange={handleChange}
              placeholder="978-4-12345-678-9"
            />
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="pages">ページ数</label>
              <input
                type="number"
                id="pages"
                name="pages"
                value={formData.pages}
                onChange={handleChange}
                min="1"
                placeholder="300"
              />
            </div>

            <div className="form-group">
              <label htmlFor="published_year">出版年</label>
              <input
                type="number"
                id="published_year"
                name="published_year"
                value={formData.published_year}
                onChange={handleChange}
                min="1000"
                max={new Date().getFullYear()}
                placeholder="2023"
              />
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="description">説明</label>
            <textarea
              id="description"
              name="description"
              value={formData.description}
              onChange={handleChange}
              rows={4}
              placeholder="本の説明を入力..."
            />
          </div>

          <div className="form-actions">
            <button type="button" onClick={onCancel} disabled={loading}>
              キャンセル
            </button>
            <button type="submit" disabled={loading}>
              {loading ? '保存中...' : (book ? '更新' : '作成')}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default BookForm;