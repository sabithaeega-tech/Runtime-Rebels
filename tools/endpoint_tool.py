import json
import os

# Path to endpoints.json
DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "endpoints.json"
)


def load_endpoints():
    """
    Load all endpoint data
    """
    with open(DATA_PATH, "r") as file:
        return json.load(file)


def search_endpoint(
        device_id=None,
        hostname=None,
        health=None):
    """
    Search endpoint details.
    """

    endpoints = load_endpoints()

    results = []

    for endpoint in endpoints:

        if device_id and endpoint["device_id"].lower() != device_id.lower():
            continue

        if hostname and hostname.lower() not in endpoint["hostname"].lower():
            continue

        if health and endpoint["health"].lower() != health.lower():
            continue

        results.append(endpoint)

    return results


def check_malware(device_id):
    """
    Check malware status of a device.
    """

    endpoints = load_endpoints()

    for endpoint in endpoints:

        if endpoint["device_id"].lower() == device_id.lower():

            return {
                "device_id": endpoint["device_id"],
                "hostname": endpoint["hostname"],
                "health": endpoint["health"],
                "malware": endpoint["malware"]
            }

    return None


def get_device_health(device_id):
    """
    Get health status of a device.
    """

    endpoints = load_endpoints()

    for endpoint in endpoints:

        if endpoint["device_id"].lower() == device_id.lower():

            return {
                "device_id": endpoint["device_id"],
                "hostname": endpoint["hostname"],
                "health": endpoint["health"]
            }

    return None