from fastapi import FastAPI
from app.endpoints import router as api_router

app = FastAPI()

# エンドポイントの登録
app.include_router(api_router)
