from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.supervisor import supervisor_agent
from agents.alert_agent import alert_agent
from agents.identity_agent import identity_agent
from agents.endpoint_agent import endpoint_agent
from agents.incident_agent import incident_agent
from agents.report_agent import report_agent


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
# Router
# -------------------------------
def route(state: AgentState):

    return state["next_agent"]


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
    }
)

workflow.add_edge("alert", END)
workflow.add_edge("identity", END)
workflow.add_edge("endpoint", END)
workflow.add_edge("incident", END)
workflow.add_edge("report", END)

graph = workflow.compile()