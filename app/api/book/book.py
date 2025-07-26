from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_books():
    return {"message": "本の一覧です"}