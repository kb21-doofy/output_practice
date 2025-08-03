# create_test_user.py - テスト用ユーザー作成スクリプト
from infrastructure.db import SessionLocal
from domain.user_service import UserService

def create_test_user():
    """テスト用のユーザーを作成"""
    db = SessionLocal()
    try:
        user_service = UserService(db)
        
        # 既存のユーザーをチェック
        existing_user = user_service.get_user_by_email("admin@example.com")
        if existing_user:
            print("✅ テスト用ユーザー 'admin@example.com' は既に存在します")
            return
        
        # テスト用ユーザーを作成
        print("🔨 テスト用ユーザーを作成中...")
        user = user_service.create_user(
            email="admin@example.com",
            name="管理者",
            password="password"
        )
        
        print(f"✅ テスト用ユーザーを作成しました:")
        print(f"   メールアドレス: {user.email}")
        print(f"   名前: {user.name}")
        print(f"   ID: {user.id}")
        
    except Exception as e:
        print(f"❌ エラー: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    create_test_user()
