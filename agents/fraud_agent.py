from tools.user_data import get_user_features
from tools.fraud_protection import calculate_fraud_score, fraud_decision


async def run_fraud_agent(state):
    user_id = state["user_id"]
    message = state["message"]

    features = get_user_features(user_id)

    if not features:
        return {
            **state,
            "fraud_score": 0.0,
            "fraud_decision": "approve"
        }

    score = calculate_fraud_score(features, message)
    decision = fraud_decision(score)

    # 🚨 BLOCK CASE
    if decision == "block":
        return {
            **state,
            "fraud_score": score,
            "fraud_decision": decision,
            "response": "🚨 Your request is flagged as suspicious and cannot be processed."
        }

    return {
        **state,
        "fraud_score": score,
        "fraud_decision": decision
    }