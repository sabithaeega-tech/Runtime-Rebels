import json
import os

# Path to users.json
DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "users.json"
)


def load_users():
    """
    Load all users from users.json
    """

    with open(DATA_PATH, "r") as file:
        return json.load(file)


def search_user(
        user_id=None,
        name=None,
        department=None,
        status=None):
    """
    Search users using different filters.
    """

    users = load_users()

    results = []

    for user in users:

        if user_id and user["user_id"].lower() != user_id.lower():
            continue

        if name and name.lower() not in user["name"].lower():
            continue

        if department and user["department"].lower() != department.lower():
            continue

        if status and user["status"].lower() != status.lower():
            continue

        results.append(user)

    return results


def get_failed_logins(user_id):
    """
    Return failed login count for a user.
    """

    users = load_users()

    for user in users:

        if user["user_id"].lower() == user_id.lower():

            return {
                "user_id": user["user_id"],
                "name": user["name"],
                "failed_logins": user["failed_logins"],
                "last_login": user["last_login"],
                "status": user["status"]
            }

    return None