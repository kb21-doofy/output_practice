export interface Book {
  id: number;
  title: string;
  author: string;
  isbn?: string;
  description?: string;
  pages?: number;
  published_year?: number;
  is_available: boolean;
  borrowed_until?: string; // 貸し出し期限（ISO文字列）
  created_at: string;
  updated_at?: string;
}

export interface CreateBookRequest {
  title: string;
  author: string;
  isbn?: string;
  description?: string;
  pages?: number;
  published_year?: number;
}

export interface UpdateBookRequest {
  title?: string;
  author?: string;
  isbn?: string;
  description?: string;
  pages?: number;
  published_year?: number;
}