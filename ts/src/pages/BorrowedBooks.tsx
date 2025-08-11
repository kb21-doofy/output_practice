import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import BorrowedBookList from '../components/BorrowedBookList';
import './BorrowedBooks.css';

const BorrowedBooks: React.FC = () => {
  const navigate = useNavigate();
  const { user, logout } = useAuth();

  const handleLogout = () => {
    if (window.confirm('ログアウトしますか？')) {
      logout();
      navigate('/login');
    }
  };

  return (
    <div className="borrowed-books-page">
      <header className="app-header">
        <h1>📚 本管理システム</h1>
        <nav className="main-navigation">
          <Link to="/" className="nav-link">
            📖 全ての本
          </Link>
          <Link to="/borrowed" className="nav-link active">
            📚 貸出中の本
          </Link>
        </nav>
        <div className="header-actions">
          <div className="user-info">
            <span className="welcome-text">ようこそ、{user?.name}さん</span>
            <span className="username">({user?.email})</span>
          </div>
          <button className="logout-btn" onClick={handleLogout}>
            ログアウト
          </button>
        </div>
      </header>

      <main>
        <BorrowedBookList />
      </main>
    </div>
  );
};

export default BorrowedBooks;