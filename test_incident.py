from tools.incident_tool import *

print("Existing Incidents\n")

print(search_incident(status="Open")[:3])

print("\n-----------------------\n")

new_incident = create_incident(
    title="Suspicious PowerShell Execution",
    priority="High",
    assigned_to="SOC-A"
)

print("Created Incident")

print(new_incident)

print("\n-----------------------\n")

updated = update_incident_status(
    new_incident["incident_id"],
    "Investigating"
)

print(updated)

print("\n-----------------------\n")

critical = escalate_incident(
    new_incident["incident_id"]
)

print(critical)