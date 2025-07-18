FROM python:3.10-slim

# 作業ディレクトリの設定
WORKDIR /app

# uvインストール（グローバルに）
RUN pip install uv

# pyproject.tomlとuv.lockを先にコピー
COPY pyproject.toml uv.lock ./

# 仮想環境の作成と依存関係のインストール
RUN uv venv && uv pip install -r <(uv pip freeze)

# アプリケーションのコードをコピー
COPY . .

# FastAPIのポートを公開
EXPOSE 8000

# アプリの起動コマンド
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]