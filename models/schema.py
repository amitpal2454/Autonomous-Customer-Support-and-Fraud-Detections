# Auto-generated
from typing import TypedDict, Optional
from models.enums import Intent, AgentRoute, FraudDecision, OfferType

class CustomerState(TypedDict, total=False):
    user_id: str
    message: str

    # classification
    intent: Optional[Intent]

    # routing
    route: Optional[AgentRoute]

    # fraud
    fraud_score: Optional[float]
    fraud_decision: Optional[FraudDecision]

    # retention
    offer: Optional[OfferType]

    # final response
    response: Optional[str]