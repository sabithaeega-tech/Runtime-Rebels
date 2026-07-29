import json
import os

# Path to incidents.json
DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "incidents.json"
)


def load_incidents():
    """
    Load all incidents.
    """
    with open(DATA_PATH, "r") as file:
        return json.load(file)


def save_incidents(incidents):
    """
    Save incidents back to JSON.
    """
    with open(DATA_PATH, "w") as file:
        json.dump(incidents, file, indent=4)


def search_incident(
        incident_id=None,
        priority=None,
        status=None):
    """
    Search incidents.
    """

    incidents = load_incidents()

    results = []

    for incident in incidents:

        if incident_id and incident["incident_id"].lower() != incident_id.lower():
            continue

        if priority and incident["priority"].lower() != priority.lower():
            continue

        if status and incident["status"].lower() != status.lower():
            continue

        results.append(incident)

    return results


def create_incident(title, priority, assigned_to):
    """
    Create a new incident.
    """

    incidents = load_incidents()

    new_id = f"INC{len(incidents)+1:04}"

    new_incident = {
        "incident_id": new_id,
        "title": title,
        "priority": priority,
        "assigned_to": assigned_to,
        "status": "Open"
    }

    incidents.append(new_incident)

    save_incidents(incidents)

    return new_incident


def update_incident_status(
        incident_id,
        new_status):
    """
    Update incident status.
    """

    incidents = load_incidents()

    for incident in incidents:

        if incident["incident_id"].lower() == incident_id.lower():

            incident["status"] = new_status

            save_incidents(incidents)

            return incident

    return None


def escalate_incident(incident_id):
    """
    Escalate an incident.
    """

    incidents = load_incidents()

    for incident in incidents:

        if incident["incident_id"].lower() == incident_id.lower():

            incident["priority"] = "Critical"

            save_incidents(incidents)

            return incident

    return None