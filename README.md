# Agentic_ai_demo-
# 🤖 Agentic AI Demo — Goal → Tool → Guardrail Foundation

This project demonstrates the **foundation of Agentic AI systems** using **LangChain**, **LangGraph**, **LangSmith**, and **Guardrails-AI**.  
It showcases how an autonomous agent can take a **goal**, decide which **tools** to use, execute them, and apply **guardrails** to ensure safe, explainable, and controlled outcomes.

---

## 🚀 Features

-  **Goal-driven Agent** — The agent starts from a natural-language goal
- **Tool Integration** — Executes predefined tools like web search and summarization.
- **Guardrail System** — Checks for PII, toxicity, or unsafe responses using `guardrails-ai`.
-  **LangGraph Workflow** — Defines the agentic flow as a directed graph of actions and checks.
- **LangSmith Tracing** — Full observability of agent decisions, inputs/outputs, and tool usage in the [LangSmith UI](https://smith.langchain.com).
-  **Hugging Face + Transformers** — Uses local models for summarization (e.g., `facebook/bart-large-cnn`).
-  **OpenAI / Hugging Face API Ready** — Pluggable LLM integration for goal reasoning or summarization.

---

##  Architecture Overview

```text
GOAL (user request)
   ↓
TOOLS (functions, APIs, models)
   ↓
GUARDRAILS (safety checks)
   ↓
AGENT (LangGraph workflow)
   ↓
MONITORING (LangSmith traces)

## **Install dependencies**
pip install -U langchain langgraph langsmith guardrails-ai transformers torch openai python-dotenv

