# app/domain/user_service.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from domain.user import User
from core.auth import get_password_hash, verify_password
from typing import Optional

class UserService:
    def __init__(self, db: Session):
        self.db = db
    
    def create_user(self, email: str, name: str, password: str) -> User:
        """
        新しいユーザーを作成する
        
        Args:
            email: メールアドレス（一意）
            name: 表示名
            password: プレーンテキストパスワード（ハッシュ化される）
            
        Returns:
            User: 作成されたユーザーオブジェクト
            
        Raises:
            ValueError: メールアドレスが既に存在する場合
        """
        # パスワードをハッシュ化
        hashed_password = get_password_hash(password)
        
        # 新しいユーザーオブジェクトを作成
        new_user = User(
            email=email,
            name=name,
            hashed_password=hashed_password
        )
        
        try:
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            return new_user
        except IntegrityError as e:
            self.db.rollback()
            if "email" in str(e.orig):
                raise ValueError(f"メールアドレス '{email}' は既に使用されています")
            else:
                raise ValueError("ユーザーの作成に失敗しました")
    

    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """メールアドレスでユーザーを取得"""
        return self.db.query(User).filter(User.email == email).first()
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """IDでユーザーを取得"""
        return self.db.query(User).filter(User.id == user_id).first()
    
    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """
        ユーザー認証
        
        Args:
            email: メールアドレス
            password: プレーンテキストパスワード
            
        Returns:
            User: 認証成功時はユーザーオブジェクト、失敗時はNone
        """
        user = self.get_user_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
    
    def update_user(self, user_id: int, **kwargs) -> Optional[User]:
        """ユーザー情報を更新"""
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        
        for key, value in kwargs.items():
            if hasattr(user, key):
                if key == 'password':
                    # パスワードの場合はハッシュ化
                    user.hashed_password = get_password_hash(value)
                else:
                    setattr(user, key, value)
        
        try:
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError:
            self.db.rollback()
            return None
    
    def deactivate_user(self, user_id: int) -> bool:
        """ユーザーを無効化（論理削除）"""
        user = self.get_user_by_id(user_id)
        if not user:
            return False
        
        user.is_active = False
        self.db.commit()
        return True
    
    def get_all_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        """全ユーザーを取得（ページネーション対応）"""
        return self.db.query(User).offset(skip).limit(limit).all()
