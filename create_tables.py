# create_tables.py - テーブル作成スクリプト
from app.core.database import Base
from app.domain.book import Book  # モデルをインポートしてBaseに登録
from app.infrastructure.db import engine

def create_tables():
    """すべてのテーブルを作成"""
    print("🔨 テーブルを作成中...")
    Base.metadata.create_all(bind=engine)
    print("✅ テーブル作成完了！")
    
    # 作成されたテーブル一覧を表示
    print("\n📋 作成されたテーブル:")
    for table_name in Base.metadata.tables.keys():
        print(f"  - {table_name}")

if __name__ == "__main__":
    create_tables()