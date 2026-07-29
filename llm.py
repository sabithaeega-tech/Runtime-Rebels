
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Get Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0
)

# Test
if __name__ == "__main__":
    response = llm.invoke("Introduce yourself in one sentence.")
    print(response.content)
