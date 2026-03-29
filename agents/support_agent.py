from memory.vector_memory import retrieve_similar
from tools.rag import retrieve_policy
from utils.llm import generate_response


async def run_support_agent(state):
    user_id = state["user_id"]
    query = state["message"]

    # 🔹 Memory
    past_context = retrieve_similar(user_id, query)

    history_text = ""
    if past_context:
        history_text = "\n".join([
            f"User: {p['message']} | Bot: {p['response']}"
            for p in past_context
        ])

    # 🔹 RAG
    policy = await retrieve_policy(query)

    # 🔹 Prompt (IMPORTANT)
    prompt = f"""
You are an intelligent customer support assistant.

Use the following:

Customer History:
{history_text}

Company Policy:
{policy}

User Query:
{query}

Rules:
- Follow company policy strictly
- Use past history if relevant
- Be clear and professional
- Do NOT hallucinate

Final Answer:
"""

    # 🔹 LLM Call
    response = generate_response(prompt)

    return {
        **state,
        "response": response
    }