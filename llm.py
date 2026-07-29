from dotenv import load_dotenv
from langchain_ollama import ChatOllama
import os

# Load variables from .env
load_dotenv()

# Read model name from .env
MODEL_NAME = os.getenv("OLLAMA_MODEL", "llama3.2")

# Create the LLM object
llm = ChatOllama(
    model=MODEL_NAME,
    temperature=0
)

# Test the model
if __name__ == "__main__":
    response = llm.invoke("Introduce yourself in one sentence.")
    print(response.content)