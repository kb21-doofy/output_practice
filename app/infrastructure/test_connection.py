#postgresql接続確認用のスクリプト
'''
実行コマンド python app/infrastructure/test_connection.py
'''

from sqlalchemy import text
from db import get_db  

def test_db_connection():
    db = next(get_db())
    try:
        result = db.execute(text("SELECT 1"))
        print("✅ 接続成功！結果:", result.scalar())
    except Exception as e:
        print("❌ 接続失敗:", e)
    finally:
        db.close()

if __name__ == "__main__":
    test_db_connection()