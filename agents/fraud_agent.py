# Auto-generated
from tools.fraud_protection import calculate_fraud_score
from models.enums import FraudDecision
from tools.redis_store import check_velocity
async def run_fraud_agent(state):
    user_id = state["user_id"]

    score = await calculate_fraud_score(user_id)

    if score > 0.8:
        decision = FraudDecision.BLOCK
        response = "Fraud detected. Request blocked."
    else:
        decision = FraudDecision.APPROVE
        response = "Fraud check passed."

    return {
        **state,
        "fraud_score": score,
        "fraud_decision": decision,
        "response": response
    }