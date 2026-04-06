# Auto-generated
async def calculate_fraud_score(features: dict, message: str) -> float:
    # Dummy logic (later ML model)
    
    score = 0

    # 🔹 Behavior rules
    if features["refund_count_last_30_days"] > 3:
        score += 0.3

    if features["refund_ratio"] > 0.5:
        score += 0.3

    if features["account_age_days"] < 7:
        score += 0.2

    if features["multiple_accounts_flag"] == 1:
        score += 0.2

    # 🔹 Transaction rules
    if features["last_order_value"] > 1500:
        score += 0.2

    if features["payment_method"] == "COD":
        score += 0.1

    # 🔹 Conversation signal (VERY COOL 🔥)
    if "refund" in message.lower():
        score += 0.1

    return min(score, 1.0)


def fraud_decision(score: float):
    if score > 0.7:
        return "block"
    elif score > 0.4:
        return "review"
    else:
        return "approve"