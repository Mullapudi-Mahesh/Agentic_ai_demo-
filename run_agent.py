import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = ""  # Add your LangChain API key here

from agent import run_agent

if __name__ == "__main__":
    run_agent("Explain what LangChain is and its use in AI applications.")
