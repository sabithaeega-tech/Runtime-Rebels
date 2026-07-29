from llm import llm
from prompts.system_prompt import SYSTEM_PROMPT
from tools.endpoint_tool import (
    search_endpoint,
    check_malware,
    get_device_health
)


def endpoint_agent(user_query):
    """
    Handles endpoint-related requests.
    """

    query = user_query.lower()

    device_id = None

    words = user_query.split()

    # Extract Device ID (e.g., DEV0001)
    for word in words:
        if word.upper().startswith("DEV"):
            device_id = word.upper()
            break

    if not device_id:
        return "Please provide a valid Device ID (e.g., DEV0001)."

    # Malware check request
    if "malware" in query:

        result = check_malware(device_id)

        if not result:
            return "Device not found."

        prompt = f"""
{SYSTEM_PROMPT}

User Request:
{user_query}

Malware Information:
{result}

Generate a short SOC investigation report.

Include:
- Device ID
- Malware Status
- Recommendation
"""

        response = llm.invoke(prompt)
        return response.content

    # Health check request
    if "health" in query:

        result = get_device_health(device_id)

        if not result:
            return "Device not found."

        prompt = f"""
{SYSTEM_PROMPT}

User Request:
{user_query}

Endpoint Health:
{result}

Summarize the endpoint health professionally.

Include:
- Device ID
- Health Status
- Recommendation
"""

        response = llm.invoke(prompt)
        return response.content

    # General endpoint search
    endpoints = search_endpoint(device_id=device_id)

    if not endpoints:
        return "No matching endpoint found."

    prompt = f"""
{SYSTEM_PROMPT}

User Request:
{user_query}

Endpoint Information:
{endpoints}

Provide a professional summary of the endpoint.
"""

    response = llm.invoke(prompt)

    return response.content