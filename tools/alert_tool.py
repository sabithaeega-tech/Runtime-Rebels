import json
import os

# Path to alerts.json
DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "alerts.json"
)


def load_alerts():
    """
    Load all alerts from alerts.json
    """

    with open(DATA_PATH, "r") as file:
        return json.load(file)


def search_alert(
        severity=None,
        alert_type=None,
        status=None,
        user_id=None,
        device_id=None):
    """
    Search alerts using different filters.
    """

    alerts = load_alerts()

    results = []

    for alert in alerts:

        if severity and alert["severity"].lower() != severity.lower():
            continue

        if alert_type and alert["type"].lower() != alert_type.lower():
            continue

        if status and alert["status"].lower() != status.lower():
            continue

        if user_id and alert["user_id"] != user_id:
            continue

        if device_id and alert["device_id"] != device_id:
            continue

        results.append(alert)

    return results