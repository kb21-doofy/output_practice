import axios from 'axios';
import { Book, CreateBookRequest, UpdateBookRequest } from '../types/Book';

const API_BASE_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const bookAPI = {
  // 全ての本を取得
  getBooks: async (): Promise<Book[]> => {
    const response = await api.get('/books/');
    return response.data;
  },

  // IDで本を取得
  getBook: async (id: number): Promise<Book> => {
    const response = await api.get(`/books/${id}`);
    return response.data;
  },

  // 本を作成
  createBook: async (book: CreateBookRequest): Promise<Book> => {
    const response = await api.post('/books/', book);
    return response.data;
  },

  // 本を更新
  updateBook: async (id: number, book: UpdateBookRequest): Promise<Book> => {
    const response = await api.put(`/books/${id}`, book);
    return response.data;
  },

  // 本を削除
  deleteBook: async (id: number): Promise<void> => {
    await api.delete(`/books/${id}`);
  },

  // 本を検索
  searchBooks: async (query: string): Promise<Book[]> => {
    const response = await api.get(`/books/search?q=${encodeURIComponent(query)}`);
    return response.data;
  },
};