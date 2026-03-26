# Auto-generated
from tools.offer_engine import generate_offer

async def run_retention_agent(state):
    offer = generate_offer()

    return {
        **state,
        "offer": offer,
        "response": f"Retention Agent: Offering {offer.value}"
    }