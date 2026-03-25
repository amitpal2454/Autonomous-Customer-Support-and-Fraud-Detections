# Auto-generated
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    message: str

@router.post("/chat")
async def chat(req: ChatRequest):
    # Placeholder (we will connect LangGraph later)
    return {
        "user_id": req.user_id,
        "message": req.message,
        "response": "Processing..."
    }