from dotenv import load_dotenv
from langchain_ollama import ChatOllama
import os

load_dotenv()

MODEL_NAME = os.getenv("OLLAMA_MODEL", "llama3.2")

llm = ChatOllama(
    model=MODEL_NAME,
    temperature=0
)

if __name__ == "__main__":
    response = llm.invoke("Introduce yourself in one sentence.")
    print(response.content)
