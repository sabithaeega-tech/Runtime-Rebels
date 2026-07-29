from agents.supervisor import supervisor_agent

queries = [

    "Show all critical alerts",

    "Check login history of USR0001",

    "Check endpoint DEV0005",

    "Create a new incident",

    "Generate executive summary",

    "Show MITRE ATTACK techniques"

]

for query in queries:

    agent = supervisor_agent(query)

    print(f"User : {query}")

    print(f"Supervisor Selected : {agent}")

    print("--------------------------")