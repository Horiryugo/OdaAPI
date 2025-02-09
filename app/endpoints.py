from fastapi import APIRouter, HTTPException, Request, status
from pydantic import BaseModel
from app.api_key import validate_api_key
from app.langchain_handler import generate_answer  # langchain_handler.py からインポート

class QuestionRequest(BaseModel):
    question: str
    api_key: str

class AnswerResponse(BaseModel):
    answer: str

class ErrorResponse(BaseModel):
    error: str


router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.post("/ask", response_model=AnswerResponse, responses={
    400: {"model": ErrorResponse},
    403: {"model": ErrorResponse},
})
async def ask_question(req: QuestionRequest):
    # API key 検証
    if not validate_api_key(req.api_key):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="API key is invalid")

    # 質問文が空の場合など、入力値チェック
    if not req.question or len(req.question.strip()) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid request: question is empty")

    # LangChain を利用して回答生成
    answer = generate_answer(req.question, req.api_key)  # APIキーを渡す
    return {"answer": answer}
