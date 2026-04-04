# Auto-generated
from pydantic import BaseModel
from typing import Optional

class ChatResponse(BaseModel):
    response: str
    intent: Optional[str]
    route: Optional[str]
    fraud_score: Optional[float]
    fraud_decision: Optional[str]