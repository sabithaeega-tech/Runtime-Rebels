def supervisor_agent(user_query):
    """
    Determines which specialized agent
    should handle the user's request.
    """

    query = user_query.lower()

    # Threat Intelligence Requests
    if any(word in query for word in [
        "threat",
        "ioc",
        "mitre",
        "campaign",
        "vulnerability",
        "intel"
    ]):
        return "threat"

    # Alert Requests
    if any(word in query for word in [
        "alert",
        "severity",
        "malware alert"
    ]):
        return "alert"

    # Identity Requests
    elif any(word in query for word in [
        "user",
        "login",
        "failed login",
        "authentication",
        "employee"
    ]):
        return "identity"

    # Endpoint Requests
    elif any(word in query for word in [
        "endpoint",
        "device",
        "health",
        "host",
        "malware"
    ]):
        return "endpoint"

    # Incident Requests
    elif any(word in query for word in [
        "incident",
        "create",
        "resolve",
        "resolved",
        "close",
        "closed",
        "escalate",
        "investigation",
        "case"
    ]):
        return "incident"

    
    # Reporting Requests
    elif any(word in query for word in [
        "report",
        "summary",
        "executive"
    ]):
        return "report"

    else:
        return "general"
