from tools import summarize_text, search_web
from guardrails import pii_guardrail, tone_guardrail

def run_agent(goal: str):
    print(f" Goal received: {goal}")

    # Step 1: Plan (simple)
    plan = "1. Search the web about LangChain\n2. Summarize key info\n3. Return answer"
    print(f" Plan:\n{plan}")

    # Step 2: Use tools
    data = search_web("LangChain AI framework")
    summary = summarize_text(data)

    # Step 3: Guardrails
    if not pii_guardrail(summary):
        print("Guardrail triggered: PII detected!")
        return
    if not tone_guardrail(summary):
        print("Guardrail triggered: Impolite language!")
        return

    print("Guardrails passed.")
    print("\n Final Answer:\n", summary)
