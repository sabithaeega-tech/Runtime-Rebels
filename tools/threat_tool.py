import json
import os

# Path to threat_intelligence.json
DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "threat_intelligence.json"
)


def load_threat_intel():
    """
    Load all threat intelligence entries.
    """
    with open(DATA_PATH, "r") as file:
        return json.load(file)


def search_threat_intel(query=None, ioc_type=None, threat_actor=None, mitre=None):
    """
    Search threat intelligence entries by query and metadata.
    """
    intel = load_threat_intel()
    results = []

    for entry in intel:
        if ioc_type and entry["ioc_type"].lower() != ioc_type.lower():
            continue

        if threat_actor and threat_actor.lower() not in entry["threat_actor"].lower():
            continue

        if mitre and mitre.lower() not in entry["mitre_technique"].lower():
            continue

        if query:
            lowered = query.lower()
            if (
                lowered in entry["value"].lower()
                or lowered in entry["threat_actor"].lower()
                or lowered in entry["mitre_technique"].lower()
                or lowered in entry["ioc_type"].lower()
            ):
                results.append(entry)
                continue
            else:
                continue

        results.append(entry)

    return results


def enrich_alerts_with_threat_intel(alerts):
    """
    Enrich alerts with matching threat intelligence context.
    """
    intel = load_threat_intel()
    enriched_alerts = []

    for alert in alerts:
        matches = []

        for entry in intel:
            value = entry["value"]

            if entry["ioc_type"].lower() == "ip":
                if alert.get("source_ip") == value:
                    matches.append(entry)

            elif entry["ioc_type"].lower() == "domain":
                if alert.get("type", "").lower() in ["phishing", "malware", "suspicious ip"]:
                    matches.append(entry)

            elif entry["ioc_type"].lower() == "hash":
                if alert.get("type", "").lower() in ["malware", "suspicious file", "file hash"]:
                    matches.append(entry)

        alert_copy = dict(alert)
        if matches:
            alert_copy["threat_matches"] = matches
            alert_copy["confidence_score"] = max(entry["confidence"] for entry in matches)
            alert_copy["recommendation"] = (
                "This alert has been enriched with threat intelligence. Review the linked IOCs, "
                "validate affected assets, and consider isolating the impacted endpoint."
            )
        else:
            alert_copy["threat_matches"] = []
            alert_copy["confidence_score"] = 0
            alert_copy["recommendation"] = "No direct intelligence match found for this alert."

        enriched_alerts.append(alert_copy)

    return enriched_alerts
