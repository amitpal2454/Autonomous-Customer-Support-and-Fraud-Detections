from models.schema import CustomerState
from models.enums import Intent, AgentRoute
from utils.logger import trace_node

from agents.support_agent import run_support_agent
from agents.fraud_agent import run_fraud_agent
from agents.retention_agent import run_retention_agent


# -----------------------------
# Intent Classification
# -----------------------------
@trace_node
async def classify_intent_node(state: CustomerState) -> CustomerState:
    message = state["message"].lower()

    if "refund" in message:
        intent = Intent.REFUND
    elif "issue" in message or "problem" in message:
        intent = Intent.COMPLAINT
    elif "cancel" in message:
        intent = Intent.INQUIRY
    else:
        intent = Intent.INQUIRY

    return {**state, "intent": intent}


# -----------------------------
# Routing Logic
# -----------------------------
@trace_node
async def route_node(state: CustomerState) -> CustomerState:
    intent = state.get("intent")

    if intent == Intent.REFUND:
        route = AgentRoute.FRAUD   # fraud check first
    elif intent == Intent.COMPLAINT:
        route = AgentRoute.SUPPORT
    else:
        route = AgentRoute.SUPPORT

    return {**state, "route": route}


# -----------------------------
# Agent Nodes
# -----------------------------
@trace_node
async def support_node(state: CustomerState) -> CustomerState:
    return await run_support_agent(state)


@trace_node
async def fraud_node(state: CustomerState) -> CustomerState:
    return await run_fraud_agent(state)


@trace_node
async def retention_node(state: CustomerState) -> CustomerState:
    return await run_retention_agent(state)


# -----------------------------
# Final Node
# -----------------------------
@trace_node
async def final_response_node(state: CustomerState) -> CustomerState:
    # can add formatting / logging here
    return state