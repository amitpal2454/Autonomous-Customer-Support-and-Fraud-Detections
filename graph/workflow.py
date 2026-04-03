from langgraph.graph import StateGraph, END
from models.schema import CustomerState

from graph.nodes import (
    classify_intent_node,
    route_node,
    support_node,
    fraud_node,
    retention_node,
    final_response_node
)

from graph.edges import route_decision


def build_graph():
    builder = StateGraph(CustomerState)

    # -----------------------------
    # ADD NODES FIRST
    # -----------------------------
    builder.add_node("classify", classify_intent_node)
    builder.add_node("route", route_node)

    builder.add_node("support", support_node)
    builder.add_node("fraud", fraud_node)
    builder.add_node("retention", retention_node)

    builder.add_node("final", final_response_node)  # ✅ MUST be here

    # -----------------------------
    # FLOW
    # -----------------------------
    builder.set_entry_point("classify")

    builder.add_edge("classify", "route")

    builder.add_conditional_edges(
        "route",
        route_decision,
        {
            "support": "support",
            "fraud": "fraud",
            "retention": "retention"
        }
    )

    # ✅ Now safe to use "final"
    
    builder.add_edge("fraud", "support")
    builder.add_edge("support", "final")
    builder.add_edge("retention", "final")

    builder.add_edge("final", END)
    print(builder.nodes)

    return builder.compile()


# Singleton instance
graph = build_graph()