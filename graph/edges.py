def route_decision(state):
    route = state.get("route")

    if route.value == "fraud":
        return "fraud"
    elif route.value == "retention":
        return "retention"
    else:
        return "support"