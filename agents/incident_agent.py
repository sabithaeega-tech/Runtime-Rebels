from llm import llm
from prompts.system_prompt import SYSTEM_PROMPT
from tools.incident_tool import (
    search_incident,
    create_incident,
    update_incident_status,
    escalate_incident
)


def incident_agent(user_query):
    """
    Handles incident-related requests.
    """

    query = user_query.lower()

    # -------------------------------
    # Create Incident
    # -------------------------------
    if "create" in query:

        incident = create_incident(
            title="Security Incident",
            priority="High",
            assigned_to="SOC-Team"
        )

        prompt = f"""
{SYSTEM_PROMPT}

A new security incident has been created.

Incident Details:
{incident}

Generate a professional confirmation message.

Include:
- Incident ID
- Priority
- Assigned Team
- Current Status
"""

        response = llm.invoke(prompt)

        return response.content

    # -------------------------------
    # Escalate Incident
    # -------------------------------
    elif "escalate" in query:

        incident_id = None

        for word in user_query.split():
            if word.upper().startswith("INC"):
                incident_id = word.upper()
                break

        if not incident_id:
            return "Please provide a valid Incident ID."

        incident = escalate_incident(incident_id)

        if not incident:
            return "Incident not found."

        prompt = f"""
{SYSTEM_PROMPT}

Incident Escalated

{incident}

Generate a short SOC escalation report.
"""

        response = llm.invoke(prompt)

        return response.content

    # -------------------------------
    # Update Status
    # -------------------------------
    elif "resolve" in query or "close" in query:

        incident_id = None

        for word in user_query.split():
            if word.upper().startswith("INC"):
                incident_id = word.upper()
                break

        if not incident_id:
            return "Please provide a valid Incident ID."

        incident = update_incident_status(
            incident_id,
            "Resolved"
        )

        if not incident:
            return "Incident not found."

        prompt = f"""
{SYSTEM_PROMPT}

Incident Updated

{incident}

Generate a professional resolution summary.
"""

        response = llm.invoke(prompt)

        return response.content

    # -------------------------------
    # Search Incident
    # -------------------------------
    else:

        incidents = search_incident()

        if not incidents:
            return "No incidents found."

        prompt = f"""
{SYSTEM_PROMPT}

User Request:
{user_query}

Incident Data:
{incidents[:10]}

Summarize the incidents.

Include:
- Total incidents shown
- Priority levels
- Status distribution
- Recommendations
"""

        response = llm.invoke(prompt)

        return response.content