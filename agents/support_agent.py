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
    You are a customer support assistant.

    Use ONLY the provided policy context to answer.

    Policy Context:
    {policy}

    User Query:
    {query}

    Instructions:
    - If answer is found → respond clearly
    - If partially found → explain using available info
    - If NOT found → say "Not mentioned in policy"
    - DO NOT ignore the context

    Answer:
    """

    # 🔹 LLM Call
    print("POLICY PASSED TO LLM:\n", policy)
    if not policy or policy.strip() == "":
        return {
            **state,
            "response": "No relevant policy found."
        }
    response = generate_response(prompt)

    return {
        **state,
        "response": response
    }