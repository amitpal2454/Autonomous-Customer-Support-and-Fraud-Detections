from tools.user_data import get_user_features
from tools.fraud_rules import calculate_fraud_score, fraud_decision
from tools.issue_detector import detect_issue
from tools.policy_validator import validate_policy
from tools.fraud_explainer import generate_fraud_explanation


async def run_fraud_agent(state):
    user_id = state["user_id"]
    message = state["message"]

    # 🔹 Step 1: detect issue
    issue = detect_issue(message)

    # 🔹 Step 2: get user data
    features = get_user_features(user_id)

    score, reasons = calculate_fraud_score(features, message)
    decision = fraud_decision(score)

    # 🔹 Step 3: policy validation
    policy_allowed, policy_text = await validate_policy(issue["issue_type"])

    # 🚨 Fraud Block
    if decision == "block":
        explanation = generate_fraud_explanation(features, reasons, message)

        return {
            **state,
            "fraud_score": score,
            "fraud_decision": "block",
            "fraud_reason": reasons,
            "fraud_explanation": explanation,
            "response": f"🚨 Request blocked: {explanation}"
        }

    # ❌ Policy Reject
    if not policy_allowed:
        return {
            **state,
            "fraud_score": score,
            "fraud_decision": "reject",
            "fraud_reason": ["Policy restriction"],
            "response": "❌ This request is not eligible as per policy."
        }

    # ✅ Approved → continue
    return {
        **state,
        "fraud_score": score,
        "fraud_decision": decision,
        "fraud_reason": reasons,
        "issue_type": issue["issue_type"]
    }