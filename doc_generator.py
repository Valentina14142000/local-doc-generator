from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_doc_model():
    return ChatOpenAI(
        model="smollm2-135m-instruct",
        temperature=0,
        openai_api_base="http://127.0.0.1:1234/v1",
        openai_api_key="not-needed"
    )

def analyze_code_structure(code: str) -> str:
    model = get_doc_model()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a senior technical writer. Analyze the provided source code, identify its core functions, parameters, and return types, and break down its architecture."),
        ("user", "Analyze this code:\n\n{code}")
    ])
    chain = prompt | model | StrOutputParser()
    return chain.invoke({"code": code})

def generate_markdown_docs(analysis: str) -> str:
    model = get_doc_model()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a professional documentation engineer. Convert the technical analysis into clean, production-ready Markdown documentation, including an overview, function descriptions, and usage examples."),
        ("user", "Generate markdown documentation based on this analysis:\n\n{analysis}")
    ])
    chain = prompt | model | StrOutputParser()
    return chain.invoke({"analysis": analysis})
