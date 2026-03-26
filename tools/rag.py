# Auto-generated
# tools/rag.py

async def retrieve_policy(query: str) -> str:
    # Dummy RAG (later replace with Azure AI Search)
    if "refund" in query.lower():
        return "Refunds are allowed within 7 days of purchase."
    return "Please contact support for more details."