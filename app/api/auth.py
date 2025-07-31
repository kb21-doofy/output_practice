# app/api/auth.py
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import timedelta
from core.auth import (
    authenticate_user, 
    create_access_token, 
    verify_token,
    get_user,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: dict

class UserResponse(BaseModel):
    email: str
    name: str

@router.post("/login", response_model=LoginResponse)
async def login(login_data: LoginRequest):
    """ユーザーログイン"""
    user = authenticate_user(login_data.email, login_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="メールアドレスまたはパスワードが間違っています",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "email": user["email"],
            "name": user["name"]
        }
    }

@router.get("/me", response_model=UserResponse)
async def get_current_user(current_user_email: str = Depends(verify_token)):
    """現在のユーザー情報を取得"""
    user = get_user(current_user_email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ユーザーが見つかりません"
        )
    
    return {
        "email": user["email"],
        "name": user["name"]
    }

@router.post("/logout")
async def logout():
    """ログアウト（クライアント側でトークンを削除）"""
    return {"message": "ログアウトしました"}
