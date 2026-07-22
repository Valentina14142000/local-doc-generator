# Local AI Documentation Generator 

An autonomous multi-stage documentation pipeline built using **LangGraph**, **LangChain**, and **LM Studio**. It analyzes source code structures and automatically formats them into production-ready Markdown documentation—all running completely offline and locally.

---

## Features

* **100% Offline & Private:** Operates entirely locally via LM Studio without external API leakage.
* **LangGraph Pipeline:** Modular workflow separating code structural analysis from Markdown generation.
* **Automated Technical Writing:** Converts raw classes and methods into clean overviews, function breakdowns, and usage examples.

---

## Tech Stack

* **Orchestration:** LangGraph / LangChain (`langgraph`, `langchain`, `langchain-openai`)
* **Runtime:** Python 3.9+ / Virtual Environment (`venv`)
* **Local Inference:** LM Studio (compatible with OpenAI-spec local endpoints)
