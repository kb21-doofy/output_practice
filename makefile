.PHONY: init build up down clean install-frontend dev logs

# 🚀 開発環境の初期化（一括実行）
init: build install-frontend up setup-db
	@echo "✅ 開発環境の初期化が完了しました！"
	@echo ""
	@echo "🌐 アクセス先:"
	@echo "  - フロントエンド: http://localhost:5173"
	@echo "  - バックエンドAPI: http://localhost:8000"
	@echo "  - API ドキュメント: http://localhost:8000/docs"
	@echo ""
	@echo "🛠️  開発開始:"
	@echo "  make dev  # フロントエンド開発サーバー起動"

# Docker環境のビルドと起動
build:
	@echo "🐳 Dockerコンテナをビルド中..."
	docker-compose build

up:
	@echo "🚀 Docker環境を起動中..."
	docker-compose up -d

# フロントエンドの依存関係インストール
install-frontend:
	@echo "📦 フロントエンドの依存関係をインストール中..."
	cd ts && npm install

# データベースの初期化
setup-db:
	@echo "🗃️  データベースを初期化中..."
	@echo "⏳ FastAPIアプリケーションの起動を待機中..."
	@sleep 20  # FastAPIアプリケーションの起動を待つ
	@echo "🔍 コンテナの状態を確認中..."
	@docker compose ps
	@docker exec fastapi-app uv run python app/scripts/create_tables.py

# フロントエンド開発サーバー起動
dev:
	@echo "🖥️  フロントエンド開発サーバーを起動中..."
	cd ts && npm run dev

# Docker環境の停止
down:
	@echo "🛑 Docker環境を停止中..."
	docker-compose down

# ログの表示
logs:
	docker-compose logs -f

# 環境のクリーンアップ
clean:
	@echo "🧹 環境をクリーンアップ中..."
	docker-compose down -v
	docker system prune -f
	cd ts && rm -rf node_modules
	@echo "✅ クリーンアップ完了"

# ヘルプ
help:
	@echo "📋 利用可能なコマンド:"
	@echo "  make init          - 開発環境の初期化（推奨）"
	@echo "  make dev           - フロントエンド開発サーバー起動"
	@echo "  make up            - Docker環境起動"
	@echo "  make down          - Docker環境停止"
	@echo "  make logs          - ログ表示"
	@echo "  make clean         - 環境クリーンアップ"
