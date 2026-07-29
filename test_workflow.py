from workflow.langgraph_workflow import graph

queries = [
    "Show all critical alerts",
    "Show failed login history for USR0001",
    "Check malware status of DEV0001",
    "Create a new incident",
    "Generate executive summary"
]

for query in queries:

    print("=" * 70)
    print("User:", query)

    result = graph.invoke({
        "user_query": query,
        "next_agent": "",
        "response": ""
    })

    print("\nAssistant:\n")
    print(result["response"])