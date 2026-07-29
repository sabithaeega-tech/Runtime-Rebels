from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.supervisor import supervisor_agent
from agents.alert_agent import alert_agent
from agents.identity_agent import identity_agent
from agents.endpoint_agent import endpoint_agent
from agents.incident_agent import incident_agent
from agents.report_agent import report_agent
from agents.threat_agent import threat_agent


# -------------------------------
# Workflow State
# -------------------------------
class AgentState(TypedDict):
    user_query: str
    next_agent: str
    response: str


# -------------------------------
# Supervisor Node
# -------------------------------
def supervisor_node(state: AgentState):

    query = state["user_query"]

    selected_agent = supervisor_agent(query)

    state["next_agent"] = selected_agent

    return state


# -------------------------------
# Alert Node
# -------------------------------
def alert_node(state: AgentState):

    state["response"] = alert_agent(state["user_query"])

    return state


# -------------------------------
# Identity Node
# -------------------------------
def identity_node(state: AgentState):

    state["response"] = identity_agent(state["user_query"])

    return state


# -------------------------------
# Endpoint Node
# -------------------------------
def endpoint_node(state: AgentState):

    state["response"] = endpoint_agent(state["user_query"])

    return state


# -------------------------------
# Incident Node
# -------------------------------
def incident_node(state: AgentState):

    state["response"] = incident_agent(state["user_query"])

    return state


# -------------------------------
# Report Node
# -------------------------------
def report_node(state: AgentState):

    state["response"] = report_agent(state["user_query"])

    return state


# -------------------------------
# Threat Intelligence Node
# -------------------------------
def threat_node(state: AgentState):

    state["response"] = threat_agent(state["user_query"])

    return state


# -------------------------------
# General Fallback Node
# -------------------------------
def general_node(state: AgentState):

    state["response"] = (
        "SecureOps AI can help with alerts, incidents, identity, endpoints, reports, "
        "and threat intelligence investigations. Please ask a security-focused question."
    )

    return state


# -------------------------------
# Router
# -------------------------------
def route(state: AgentState):

    next_agent = state.get("next_agent")
    if next_agent not in {
        "alert",
        "identity",
        "endpoint",
        "incident",
        "report",
        "threat",
        "general",
    }:
        next_agent = "general"

    return next_agent


# -------------------------------
# Build Graph
# -------------------------------
workflow = StateGraph(AgentState)

workflow.add_node("supervisor", supervisor_node)
workflow.add_node("alert", alert_node)
workflow.add_node("identity", identity_node)
workflow.add_node("endpoint", endpoint_node)
workflow.add_node("incident", incident_node)
workflow.add_node("report", report_node)
workflow.add_node("threat", threat_node)
workflow.add_node("general", general_node)

workflow.set_entry_point("supervisor")

workflow.add_conditional_edges(
    "supervisor",
    route,
    {
        "alert": "alert",
        "identity": "identity",
        "endpoint": "endpoint",
        "incident": "incident",
        "report": "report",
        "threat": "threat",
        "general": "general",
    }
)

workflow.add_edge("alert", END)
workflow.add_edge("identity", END)
workflow.add_edge("endpoint", END)
workflow.add_edge("incident", END)
workflow.add_edge("report", END)
workflow.add_edge("threat", END)
workflow.add_edge("general", END)

graph = workflow.compile()