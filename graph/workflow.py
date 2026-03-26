# Auto-generated
# graph/workflow.py

from langgraph.graph import StateGraph, END
from models.schema import CustomerState
from graph.nodes import (
    classify_intent_node,
    route_node,
    support_node,
    fraud_node,
    final_response_node,retention_node
)
from graph.edges import route_decision


def build_graph():
    builder = StateGraph(CustomerState)

    # Nodes
    builder.add_node("classify", classify_intent_node)
    builder.add_node("route", route_node)
    builder.add_node("support", support_node)
    builder.add_node("fraud", fraud_node)
    builder.add_node("final", final_response_node)
    builder.add_node("retention", retention_node)

    # Flow
    builder.set_entry_point("classify")
    builder.add_edge("classify", "route")

    builder.add_conditional_edges(
    "route",
        route_decision,
        {
            "support": "support",
            "fraud": "fraud",
            "retention": "retention",
        }
    )
    builder.add_edge("support", "final")
    builder.add_edge("fraud", "final")

    builder.add_edge("final", END)

    return builder.compile()


# Singleton graph
graph = build_graph()