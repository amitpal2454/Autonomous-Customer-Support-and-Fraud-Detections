import chromadb
import uuid

client = chromadb.Client()
collection = client.get_or_create_collection("memory")


def save_session(user_id, message, response):
    collection.add(
        documents=[message],
        metadatas=[{
            "user_id": user_id,
            "response": response
        }],
        ids=[str(uuid.uuid4())]
    )


def retrieve_similar(user_id, query):
    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    # filter by user_id
    filtered = []
    for i, meta in enumerate(results["metadatas"][0]):
        if meta["user_id"] == user_id:
            filtered.append({
                "message": results["documents"][0][i],
                "response": meta["response"]
            })

    return filtered