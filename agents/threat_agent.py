from llm import llm
from prompts.system_prompt import SYSTEM_PROMPT
from tools.threat_tool import search_threat_intel, load_threat_intel


def threat_agent(user_query):
    """
    Handles threat intelligence-related requests.
    """

    query = user_query.lower()

    if any(word in query for word in [
        "ioc",
        "indicator",
        "domain",
        "ip",
        "hash",
        "threat actor",
        "mitre",
        "campaign",
        "vulnerability"
    ]):
        matching_intel = search_threat_intel(query=query)
        intel_summary = matching_intel if matching_intel else load_threat_intel()[:5]
    else:
        matching_intel = load_threat_intel()[:5]
        intel_summary = matching_intel

    prompt = f"""
{SYSTEM_PROMPT}

User Request:
{user_query}

Threat Intelligence Data:
{intel_summary}

Analyze the relevant threat intelligence and explain:
- Why the threat is relevant to current investigations.
- Which assets or alerts are likely affected.
- Recommended defensive actions.
- A confidence level for the recommendation.
- Ask the analyst to approve or reject the recommendation.

Keep the answer clear, concise, and SOC-focused.
"""

    response = llm.invoke(prompt)

    return response.content
