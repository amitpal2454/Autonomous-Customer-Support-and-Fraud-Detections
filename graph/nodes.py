# Auto-generated
# graph/nodes.py

from models.schema import CustomerState
from models.enums import Intent, AgentRoute
from utils.logger import trace_node
from agents.support_agent import run_support_agent
from agents.fraud_agent import run_fraud_agent
from agents.retention_agent import run_retention_agent

@trace_node
async def classify_intent_node(state: CustomerState) -> CustomerState:
    message = state["message"].lower()

    if "refund" in message:
        intent = Intent.REFUND
    elif "issue" in message or "problem" in message:
        intent = Intent.COMPLAINT
    else:
        intent = Intent.INQUIRY

    return {**state, "intent": intent}


@trace_node
async def route_node(state: CustomerState) -> CustomerState:
    intent = state.get("intent")

    if intent == Intent.REFUND:
        route = AgentRoute.FRAUD   # first check fraud
    elif intent == Intent.COMPLAINT:
        route = AgentRoute.SUPPORT
    else:
        route = AgentRoute.SUPPORT

    return {**state, "route": route}



# Replace old nodes

async def support_node(state):
    return await run_support_agent(state)

async def fraud_node(state):
    return await run_fraud_agent(state)

async def retention_node(state):
    return await run_retention_agent(state)