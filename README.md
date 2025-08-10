# branch 運用!

## main 
- 常に動作する状態のコードのみをマージするブランチです。
- リリース可能な安定版コードを管理します。

## dev
- mainにマージする前のワンクッションとして使用する開発ブランチです。
- 新機能や修正を加えた際に、まずこのブランチで動作確認を行います。

# ディレクトリ構成

```
my-aws-project/
├── app/                    # FastAPI バックエンド
│   ├── api/               # API エンドポイント
│   ├── domain/            # ドメインモデル・サービス
│   ├── infrastructure/    # データベース接続
│   ├── core/             # 設定・共通機能
│   ├── scripts/          # データベース初期化
│   └── static/           # 静的ファイル（favicon等）
├── ts/                    # React フロントエンド
│   ├── src/
│   │   ├── components/   # Reactコンポーネント
│   │   ├── pages/        # ページコンポーネント
│   │   ├── services/     # API通信
│   │   └── types/        # TypeScript型定義
│   └── public/           # 静的アセット
├── docker-compose.yml     # Docker構成
├── Dockerfile            # FastAPIコンテナ
└── .env   


# 1. 環境構築
docker-compose up --build

# 2. フロントエンド開発サーバー起動
cd ts
npm install
npm run dev

# 3. データベース初期化
docker exec -it fastapi-app python app/scripts/create_tables.py

# 4. アクセス先
# - フロントエンド: http://localhost:5173
# - バックエンドAPI: http://localhost:8000
# - PostgreSQL: localhost:5433



# docker 

## 起動
docker-compose up --build
## 停止
- docker stop <コンテナID または 名前>



# バックエンド
## uv環境起動
- $ source .venv/bin/activate
## FastAPI起動コマンド
- $ uvicorn main:app --reload
## uv ライブラリ追加
- uv add <パッケージ名>
## pyproject.tomlを見て依存パッケージを同期
- uv sync



# フロントエンド
## npmのinstall
- $ npm install
## npm起動
- $ npm run dev



# データベース
## 接続確認コマンド
- $ uv run python -m app.scripts.test_crud
## postgret起動
- $  psql -U postgres -d booklog
## テーブル一覧表示する
- \dt   
## テーブル定義確認
- \d {テーブル名}
## データベース変更
- \c {データベース名}
# スクリプト実行にてテーブル作成(* app配下で実行)
- python -m scripts.create_tables

