from llm import llm
from prompts.system_prompt import SYSTEM_PROMPT
from tools.alert_tool import search_alert


def alert_agent(user_query):
    """
    Handles security alert-related requests.
    """

    query = user_query.lower()

    severity = None

    if "critical" in query:
        severity = "Critical"

    elif "high" in query:
        severity = "High"

    elif "medium" in query:
        severity = "Medium"

    elif "low" in query:
        severity = "Low"

    alerts = search_alert(severity=severity)

    if not alerts:
        return "No matching alerts were found."

    prompt = f"""
{SYSTEM_PROMPT}

User Request:
{user_query}

Alert Data:
{alerts}

Summarize the alerts in a professional SOC report.
Mention:

1. Total alerts found
2. Severity
3. Alert Type
4. Device
5. Status

Keep the answer short.
"""

    response = llm.invoke(prompt)

    return response.content