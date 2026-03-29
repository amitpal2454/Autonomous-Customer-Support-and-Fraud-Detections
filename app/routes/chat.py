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
    from memory.vector_memory import save_session

    result = await graph.ainvoke(state)

    save_session(
        req.user_id,
        req.message,
        result.get("response")
    )