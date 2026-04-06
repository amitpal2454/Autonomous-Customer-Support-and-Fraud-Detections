from fastapi import APIRouter
from pydantic import BaseModel
from graph.workflow import graph
from models.api_models import ChatResponse
from utils.serialiser import to_str
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

    from memory.vector_memory import save_session

    result = await graph.ainvoke(state)

    print("Final Result:", result)

    # 🚨 Block handling
    if result.get("fraud_decision") == "block":
        return {
            "response": result.get("response"),
            "intent": result.get("intent").value if result.get("intent") else None,
            "route": result.get("route").value if result.get("route") else None,
            "fraud_score": float(result.get("fraud_score", 0)),
            "fraud_decision": "block",
            "fraud_reason": result.get("fraud_reason", "")
        }

    # ✅ Save only valid interactions
    save_session(
        req.user_id,
        req.message,
        result.get("response")
    )

    return {
    "response": result.get("response", ""),
    "intent": to_str(result.get("intent")),
    "route": to_str(result.get("route")),
    "fraud_score": float(result.get("fraud_score", 0)),
    "fraud_decision": to_str(result.get("fraud_decision")),
    "fraud_reason": result.get("fraud_reason", "")
}