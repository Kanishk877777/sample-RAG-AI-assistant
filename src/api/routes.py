from fastapi import APIRouter
from pydantic import BaseModel
from src.legal_ques import ask_legal_question

router = APIRouter()


class Query(BaseModel):
    query: str


@router.post('/ask')
def ask(request: Query):
    answer = ask_legal_question(request.query)
    return {"answer": str(answer)}
