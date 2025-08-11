import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import { useAuth } from '../contexts/AuthContext'
import type { Book } from '../types/Book'
import BookList from '../components/BookList'
import BookForm from '../components/BookForm'
import './Home.css'

function Home() {
  const navigate = useNavigate()
  const { user, logout } = useAuth()
  const [showForm, setShowForm] = useState(false)
  const [editingBook, setEditingBook] = useState<Book | undefined>(undefined)
  const [refreshTrigger, setRefreshTrigger] = useState(0)

  const handleAddBook = () => {
    setEditingBook(undefined)
    setShowForm(true)
  }

  const handleEditBook = (book: Book) => {
    setEditingBook(book)
    setShowForm(true)
  }

  const handleFormSuccess = () => {
    setShowForm(false)
    setEditingBook(undefined)
    setRefreshTrigger(prev => prev + 1)
  }

  const handleFormCancel = () => {
    setShowForm(false)
    setEditingBook(undefined)
  }

  const handleLogout = () => {
    if (window.confirm('ログアウトしますか？')) {
      logout()
      navigate('/login')
    }
  }

  return (
    <div className="home">
      <header className="app-header">
        <h1>📚 本管理システム</h1>
        <nav className="main-navigation">
          <Link to="/" className="nav-link active">
            📖 全ての本
          </Link>
          <Link to="/borrowed" className="nav-link">
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
          <button className="add-book-btn" onClick={handleAddBook}>
            + 新しい本を追加
          </button>
        </div>
      </header>

      <main>
        <BookList
          onEditBook={handleEditBook}
          refreshTrigger={refreshTrigger}
        />
      </main>

      {showForm && (
        <BookForm
          book={editingBook}
          onSuccess={handleFormSuccess}
          onCancel={handleFormCancel}
        />
      )}
    </div>
  )
}

export default Home