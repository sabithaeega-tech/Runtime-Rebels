from tools.alert_tool import search_alert

results = search_alert(severity="Critical")

print(f"Found {len(results)} alerts\n")

for alert in results[:5]:
    print(alert)