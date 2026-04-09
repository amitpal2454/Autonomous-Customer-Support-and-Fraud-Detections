from utils.llm import generate_response


def generate_fraud_explanation(features, reasons, message):
    prompt = f"""
You are a fraud detection AI.

User message:
{message}

User features:
{features}

Detected risk signals:
{reasons}

Explain in simple business language:
- Why this request may be risky
- Keep it short (2-3 lines)
"""

    return generate_response(prompt)