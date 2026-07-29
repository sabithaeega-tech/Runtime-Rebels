from memory.memory import memory

memory.save_context(
    {"input": "Show all alerts"},
    {"output": "Found 5 alerts"}
)

print(memory.load_memory_variables({}))