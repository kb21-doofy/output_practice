import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Login.css';

const Login: React.FC = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!formData.email.trim() || !formData.password.trim()) {
      setError('メールアドレスとパスワードを入力してください');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      // TODO: 実際のログイン処理をここに実装
      // 現在は仮のログイン処理
      await new Promise(resolve => setTimeout(resolve, 1000)); // 1秒待機
      
      // 仮のログイン成功処理
      if (formData.email === 'admin@example.com' && formData.password === 'password') {
        alert('ログイン成功！');
        navigate('/'); // メインページに遷移
      } else {
        setError('メールアドレスまたはパスワードが間違っています');
      }
    } catch (err) {
      setError('ログインに失敗しました');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-page">
      <div className="login-container">
        <div className="login-header">
          <h1>📚 本管理システム</h1>
          <h2>ログイン</h2>
        </div>

        <form onSubmit={handleSubmit} className="login-form">
          {error && <div className="error-message">{error}</div>}

          <div className="form-group">
            <label htmlFor="email">メールアドレス</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="admin@example.com"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="password">パスワード</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              placeholder="password"
              required
            />
          </div>

          <button type="submit" className="login-btn" disabled={loading}>
            {loading ? 'ログイン中...' : 'ログイン'}
          </button>
        </form>

        <div className="login-footer">
          <p>テスト用アカウント:</p>
          <p>Email: admin@example.com</p>
          <p>Password: password</p>
          <button 
            className="back-btn" 
            onClick={() => navigate('/')}
          >
            本管理画面に戻る
          </button>
        </div>
      </div>
    </div>
  );
};

export default Login;