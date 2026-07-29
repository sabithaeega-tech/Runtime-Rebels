from tools.identity_tool import search_user
from tools.identity_tool import get_failed_logins

print("Search by Department\n")

users = search_user(department="IT")

print(f"Found {len(users)} users\n")

for user in users[:5]:
    print(user)

print("\n----------------------\n")

print(get_failed_logins("USR0001"))