from tools.rag import retrieve_policy


async def validate_policy(issue_type: str):
    query = f"Is refund allowed for {issue_type}?"

    policy = await retrieve_policy(query)

    if "not allowed" in policy.lower():
        return False, policy

    return True, policy