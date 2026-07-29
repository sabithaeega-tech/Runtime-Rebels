from llm import llm
from prompts.system_prompt import SYSTEM_PROMPT
from tools.alert_tool import search_alert
from tools.threat_tool import enrich_alerts_with_threat_intel


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

    if any(word in user_query.lower() for word in [
        "threat",
        "ioc",
        "mitre",
        "vulnerability",
        "intel",
        "campaign"
    ]):
        alerts = enrich_alerts_with_threat_intel(alerts)
        threat_context = "\nThreat Enrichment:\n" + str(alerts)
    else:
        threat_context = ""

    prompt = f"""
{SYSTEM_PROMPT}

User Request:
{user_query}

Alert Data:
{alerts}
{threat_context}

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