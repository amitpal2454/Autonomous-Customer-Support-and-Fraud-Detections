from pinecone import Pinecone
from utils.config import get_settings

settings = get_settings()

pc = Pinecone(api_key=settings.pinecone_api_key)
index = pc.Index(settings.pinecone_index)


async def retrieve_policy(query: str):
    response = index.query(
        vector=[],  # will replace with embedding
        top_k=3,
        include_metadata=True
    )

    if response.matches:
        return response.matches[0].metadata.get("text", "")

    return "No relevant policy found."