from tools.endpoint_tool import search_endpoint
from tools.endpoint_tool import check_malware
from tools.endpoint_tool import get_device_health

print("Healthy Devices\n")

devices = search_endpoint(health="Healthy")

print(f"Found {len(devices)} healthy devices\n")

for device in devices[:5]:
    print(device)

print("\n------------------------")

print(check_malware("DEV0001"))

print("\n------------------------")

print(get_device_health("DEV0001"))