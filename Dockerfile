FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv && uv pip install -r requirements.txt || true

COPY . .

# ⑥ ポートを公開（FastAPI: 8000）
EXPOSE 8000

# ⑦ コンテナ実行時のコマンド
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]