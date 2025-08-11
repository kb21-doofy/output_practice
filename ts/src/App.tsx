import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/Login'
import Register from './pages/Register'
import BorrowedBooks from './pages/BorrowedBooks'
import { AuthProvider } from './contexts/AuthContext'
import AuthGuard from './components/AuthGuard'
import './App.css'

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="app">
          <Routes>
            <Route path="/" element={
              <AuthGuard>
                <Home />
              </AuthGuard>
            } />
            <Route path="/borrowed" element={
              <AuthGuard>
                <BorrowedBooks />
              </AuthGuard>
            } />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
          </Routes>
        </div>
      </Router>
    </AuthProvider>
  )
}

export default App