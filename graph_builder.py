from langgraph.graph import Graph, END
from tools import summarize_text, search_web
from guardrails import pii_guardrail

graph = Graph()

@graph.node
def search_node(state):
    return {"data": search_web("LangChain AI")}

@graph.node
def summarize_node(state):
    text = state["data"]
    return {"summary": summarize_text(text)}

@graph.node
def guardrail_node(state):
    if pii_guardrail(state["summary"]):
        print("Passed Guardrail")
        return {"result": state["summary"]}
    else:
        print(" Failed Guardrail")
        return {"result": "Blocked by Guardrail"}

graph.connect("search_node", "summarize_node")
graph.connect("summarize_node", "guardrail_node")
graph.connect("guardrail_node", END)
