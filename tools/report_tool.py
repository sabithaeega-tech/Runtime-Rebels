import json
import os
from datetime import datetime

# Path to reports.json
DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "reports.json"
)


def load_reports():
    """
    Load all reports.
    """
    with open(DATA_PATH, "r") as file:
        return json.load(file)


def save_reports(reports):
    """
    Save reports back to JSON.
    """
    with open(DATA_PATH, "w") as file:
        json.dump(reports, file, indent=4)


def search_report(report_id=None, incident_id=None):
    """
    Search reports.
    """

    reports = load_reports()

    results = []

    for report in reports:

        if report_id and report["report_id"].lower() != report_id.lower():
            continue

        if incident_id and report["incident_id"].lower() != incident_id.lower():
            continue

        results.append(report)

    return results


def generate_report(incident_id, summary):
    """
    Generate a new investigation report.
    """

    reports = load_reports()

    new_id = f"REP{len(reports)+1:04}"

    report = {
        "report_id": new_id,
        "incident_id": incident_id,
        "summary": summary,
        "generated_by": "SecureOps AI",
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    reports.append(report)

    save_reports(reports)

    return report


def generate_executive_summary():
    """
    Generate an executive summary.
    """

    reports = load_reports()

    summary = {
        "total_reports": len(reports),
        "generated_by": "SecureOps AI",
        "generated_on": datetime.now().strftime("%Y-%m-%d")
    }

    return summary