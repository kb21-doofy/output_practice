export interface Book {
  id: number;
  title: string;
  author: string;
  isbn?: string;
  description?: string;
  pages?: number;
  published_year?: number;
  is_available: boolean;
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