from agents.incident_agent import incident_agent

print("===== CREATE INCIDENT =====")
print(incident_agent("Create a new incident"))

print("\n" + "=" * 60 + "\n")

print("===== ESCALATE INCIDENT =====")
print(incident_agent("Escalate INC0001"))

print("\n" + "=" * 60 + "\n")

print("===== RESOLVE INCIDENT =====")
print(incident_agent("Resolve INC0001"))

print("\n" + "=" * 60 + "\n")

print("===== SEARCH INCIDENTS =====")
print(incident_agent("Show all incidents"))