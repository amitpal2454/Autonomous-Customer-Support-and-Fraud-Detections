import chromadb
from utils.llm import get_embedding


import os

DB_PATH = os.path.abspath("data/chroma_db")

print("CHROMA PATH:", DB_PATH)

client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection("policy_docs")

def classify_query(query: str):
    q = query.lower()

    if "refund" in q:
        return "refund"
    elif "return" in q:
        return "return"
    elif "fraud" in q:
        return "fraud"
    elif "exchange" in q:
        return "exchange"
    else:
        return None


async def retrieve_policy(query: str):
    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    print("RAG Results:", results)

    docs = results["documents"][0]

# take top 2 relevant chunks
    docs = docs[:2]

    policy_text = "\n\n".join(docs)

    return policy_text

    #return "No relevant policy found."