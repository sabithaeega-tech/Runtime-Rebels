from tools.report_tool import *

print("Existing Reports")

print(search_report()[:2])

print("\n--------------------\n")

new_report = generate_report(
    incident_id="INC0001",
    summary="Malware contained successfully. Endpoint isolated."
)

print("Generated Report")

print(new_report)

print("\n--------------------\n")

print(generate_executive_summary())