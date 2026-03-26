# Auto-generated
from tools.rag import retrieve_policy

async def run_support_agent(state):
    query = state["message"]

    policy = await retrieve_policy(query)

    return {
        **state,
        "response": f"Support Agent: {policy}"
    }