# SecureOps AI

A Streamlit-based Security Operations Center assistant for SecureTech Solutions.

## Overview

SecureOps AI provides an AI-powered SOC interface that routes analyst queries to specialized security workflows for alerts, incidents, identity, endpoints, reports, and threat intelligence.

The app uses:
- Python
- Streamlit
- LangGraph workflow routing
- Langchain + Ollama for LLM responses
- Local JSON data sources for alerts, incidents, endpoints, users, reports, and threat intelligence

## Key Features

- Multi-domain question routing via `agents/supervisor.py`
- Threat intelligence search and enrichment via `agents/threat_agent.py` and `tools/threat_tool.py`
- Alert, identity, endpoint, incident, and report handling through agent modules
- SecureOps AI chat interface with analyst feedback capture
- Threat intelligence dashboard card in the Streamlit UI

## Repository Structure

- `app.py` — main Streamlit application
- `llm.py` — LLM client configuration
- `workflow/langgraph_workflow.py` — supervisor workflow and routing graph
- `agents/` — specialized agent handlers
- `tools/` — data lookup and enrichment helpers
- `prompts/system_prompt.py` — shared SOC assistant prompt
- `data/` — JSON data sources
- `test_*` — lightweight test scripts

## Requirements

Install required packages:

```bash
pip install -r requirements.txt
```

## Environment

Create a `.env` file with the following values:

```env
OLLAMA_MODEL=llama3.2
EMBEDDING_MODEL=nomic-embed-text
LANGCHAIN_TRACING_V2=false
LANGCHAIN_PROJECT=SecureOpsAI
```

If using Ollama locally, ensure the model is available.

## Run the app

From the repository root:

```bash
streamlit run app.py
```

## How it works

1. User submits a query in the chat interface.
2. `workflow/langgraph_workflow.py` invokes `agents.supervisor.py`.
3. The supervisor selects the best agent based on keywords.
4. The selected agent queries data sources and asks the LLM for a response.
5. The chat response is displayed, and analyst feedback can be recorded.

## Threat Intelligence

- `tools/threat_tool.py` loads threat intelligence entries.
- `agents/threat_agent.py` searches and summarizes relevant threat intel.
- `agents/alert_agent.py` optionally enriches alerts with threat intelligence when the user asks about threat context.

## Notes

- The analyst feedback flow currently stores responses only in session state.
- Tests are currently lightweight and may need expanded assertions for production readiness.

## Suggested next steps

- Add proper unit tests for supervisor routing and threat intelligence behavior.
- Persist analyst feedback outside the session.
- Expand threat enrichment across incidents, endpoints, and reports.

## Results

<img width="1909" height="944" alt="Screenshot 2026-07-29 141057" src="https://github.com/user-attachments/assets/fb28bbfc-d20f-4835-9a2a-10e566e9eb80" />

<img width="1919" height="927" alt="image" src="https://github.com/user-attachments/assets/05f4630d-a60b-4056-9586-dd65fc66b375" />

<img width="1918" height="931" alt="image" src="https://github.com/user-attachments/assets/ce71232e-d788-45bc-8f7f-5d06c0182622" />

<img width="1891" height="937" alt="image" src="https://github.com/user-attachments/assets/a323c759-79c9-43f8-a148-e4f488893653" />

## Host Link

Local URL: http://localhost:8501
Network URL: http://172.17.36.63:8501

