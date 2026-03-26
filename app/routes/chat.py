from fastapi import APIRouter
from pydantic import BaseModel
from graph.workflow import graph

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    message: str


@router.post("/chat", tags=["Chat"])
async def chat(req: ChatRequest):
    state = {
        "user_id": req.user_id,
        "message": req.message
    }

    # 🔥 CALL LANGGRAPH
    result = await graph.ainvoke(state)

    return {
        "response": result.get("response"),
        "intent": result.get("intent"),
        "route": result.get("route"),
        "fraud_score": result.get("fraud_score")
    }