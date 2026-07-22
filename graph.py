from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from doc_generator import analyze_code_structure, generate_markdown_docs

class DocState(TypedDict):
    source_code: str
    analysis: str
    markdown_docs: str

def create_doc_graph():
    def analyze_node(state: DocState):
        analysis = analyze_code_structure(state["source_code"])
        return {"analysis": analysis}

    def format_node(state: DocState):
        docs = generate_markdown_docs(state["analysis"])
        return {"markdown_docs": docs}

    workflow = StateGraph(DocState)
    workflow.add_node("analyze_code", analyze_node)
    workflow.add_node("format_docs", format_node)

    workflow.add_edge(START, "analyze_code")
    workflow.add_edge("analyze_code", "format_docs")
    workflow.add_edge("format_docs", END)

    return workflow.compile()
