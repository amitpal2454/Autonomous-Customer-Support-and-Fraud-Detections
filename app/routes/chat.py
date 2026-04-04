from fastapi import APIRouter
from pydantic import BaseModel
from graph.workflow import graph
from models.api_models import ChatResponse
router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    message: str


@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    state = {
        "user_id": req.user_id,
        "message": req.message
    }

    # 🔥 CALL LANGGRAPH
    from memory.vector_memory import save_session

    result = await graph.ainvoke(state)

    print("Final Result:",result)

    save_session(
        req.user_id,
        req.message,
        result.get("response")
    )

    return {
    "response": result.get("response"),
    "intent": result.get("intent").value if result.get("intent") else None,
    "route": result.get("route").value if result.get("route") else None,
    "fraud_score": result.get("fraud_score"),
    "fraud_decision": result.get("fraud_decision").value if result.get("fraud_decision") else None
    }
    