# branch 運用

## main 
- 常に動作する状態のコードのみをマージするブランチです。
- リリース可能な安定版コードを管理します。

## dev
- mainにマージする前のワンクッションとして使用する開発ブランチです。
- 新機能や修正を加えた際に、まずこのブランチで動作確認を行います。

## feature/aws/handson
- AWSのCloudFormationハンズオン実施時に作成した機能ブランチです。
- ディレクトリ構成の準備後にすぐ切られており、ハンズオン内容以外の変更は加えていません。



# ディレクトリ構成

```
my-aws-project/
├── Dockerfile                 # アプリケーションのDockerイメージ定義
├── README.md                  # プロジェクト概要・運用方法
├── app/                       # FastAPIアプリケーション（バックエンド）
│   ├── api/                   # API エンドポイント
│   │   └── v1/
│   │       └── book.py        # 書籍API
│   ├── core/                  # コア機能
│   │   └── database.py        # データベース設定
│   ├── domain/                # ドメインロジック
│   │   ├── book.py            # 書籍モデル
│   │   └── book_service.py    # 書籍サービス
│   ├── infrastructure/        # インフラ層
│   │   ├── db.py              # データベース接続
│   │   └── test_connection.py # 接続テスト
│   └── main.py                # FastAPIアプリケーション起動
├── cfn/                       # CloudFormationテンプレート
│   ├── 01_vpc.yml             # VPC作成
│   ├── 02_ec2.yml             # EC2インスタンス作成
│   ├── 02_ec2_userdata.sh     # EC2初期化スクリプト
│   ├── 03_rds.yml             # RDS作成
│   └── 04_elb.yml             # ELB作成
├── create_tables.py           # データベーステーブル作成
├── docker-compose.yml         # Docker Compose設定
├── main.py                    # アプリケーションメイン
├── package-lock.json          # npm依存関係ロック（ルート）
├── pyproject.toml             # Pythonプロジェクト設定
├── templates/                 # テンプレートファイル
├── terraform/                 # Terraformファイル（未使用）
├── test_crud.py               # CRUD操作テスト
├── ts/                        # TypeScript/React アプリケーション（フロントエンド）
│   ├── README.md              # フロントエンド用README
│   ├── eslint.config.js       # ESLint設定
│   ├── index.html             # エントリーポイントHTML
│   ├── node_modules/          # npm依存関係
│   ├── package-lock.json      # npm依存関係ロック
│   ├── package.json           # npm設定
│   ├── public/                # 静的ファイル
│   │   └── vite.svg           # Viteロゴ
│   ├── src/                   # Reactソースコード
│   │   ├── App.css            # アプリケーションスタイル
│   │   ├── App.tsx            # メインアプリケーションコンポーネント
│   │   ├── assets/            # 静的アセット
│   │   │   └── react.svg      # Reactロゴ
│   │   ├── index.css          # グローバルスタイル
│   │   ├── main.tsx           # Reactエントリーポイント
│   │   └── vite-env.d.ts      # Vite型定義
│   ├── tsconfig.app.json      # TypeScript設定（アプリケーション）
│   ├── tsconfig.json          # TypeScript設定（ベース）
│   ├── tsconfig.node.json     # TypeScript設定（Node.js）
│   └── vite.config.ts         # Vite設定
├── uv.lock                    # uv依存関係ロック
└── views/                     # ビューファイル
```

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



# DB接続確認コマンド
- $ uv run python -m app.scripts.test_crud