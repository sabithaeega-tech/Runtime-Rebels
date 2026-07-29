from llm import llm
from prompts.system_prompt import SYSTEM_PROMPT
from tools.identity_tool import search_user, get_failed_logins


def identity_agent(user_query):
    """
    Handles identity and user-related requests.
    """

    query = user_query.lower()

    user_id = None

    words = user_query.split()

    for word in words:

        if word.upper().startswith("USR"):
            user_id = word.upper()
            break

    # Check failed login request
    if "failed" in query or "login" in query:

        if user_id:

            result = get_failed_logins(user_id)

            if not result:
                return "User not found."

            prompt = f"""
{SYSTEM_PROMPT}

User Request:
{user_query}

User Login Information:
{result}

Explain the login history professionally.

Mention:

- User Name
- Account Status
- Failed Logins
- Last Login
- Recommendation

Keep it short.
"""

            response = llm.invoke(prompt)

            return response.content

    # General user search

    users = search_user(user_id=user_id)

    if not users:
        return "No matching users found."

    prompt = f"""
{SYSTEM_PROMPT}

User Request:
{user_query}

User Information:
{users[:10]}

Summarize the user information professionally.
"""

    response = llm.invoke(prompt)

    return response.content