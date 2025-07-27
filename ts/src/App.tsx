import { useState } from 'react'
import type { Book } from './types/Book'
import BookList from './components/BookList'
import BookForm from './components/BookForm'
import './App.css'

function App() {
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

  return (
    <div className="app">
      <header className="app-header">
        <h1>📚 本管理システム</h1>
        <button className="add-book-btn" onClick={handleAddBook}>
          + 新しい本を追加
        </button>
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

export default App
