# Enterprise Document Search RAG Agent

A production-grade, event-driven Retrieval-Augmented Generation (RAG) agent built with **LangGraph**, **LangChain**, **Google Gemini**, and **FAISS**.

---

## 📌 Project Overview

This repository provides an enterprise-ready AI Agent architecture for document retrieval and knowledge base updates. Unlike flat scripts or standard LLM chains, this system uses **LangGraph** to manage stateful tool routing, dynamic in-memory vector store indexing, and automated evaluation.

### Key Capabilities
* **Semantic Search:** Fast, similarity-based document search using FAISS and Google Gemini Embeddings.
* **Stateful Execution:** Managed multi-step workflows powered by LangGraph `MessagesState`.
* **Dynamic Knowledge Ingestion:** On-the-fly indexing of context and documents during execution.
* **Enterprise Architecture:** Standardized Python `src/` layout to isolate business logic, settings, vector databases, and tools.
* **Automated Evaluation:** Built-in benchmarking suite for latency tracking, tool routing validation, and response accuracy checks.

---

## 🏗️ Repository Architecture

The project follows the standard enterprise Python packaging layout (`src/` structure) to prevent import shadowing and maintain clean separation of concerns:

```text
enterprise-docsearch-rag/
├── .env.example                 # Template for required environment secrets
├── .gitignore                   # Excludes bytecode, venvs, and secrets from Git
├── README.md                    # Project documentation
├── requirements.txt             # Operational dependencies
├── pyproject.toml               # Tooling and package build settings
│
├── src/                         # Application source code
│   └── enterprise_rag/          # Core Python package namespace
│       ├── __init__.py          # Marks folder as Python package
│       ├── config.py            # Environment parameters & model configurations
│       │
│       ├── core/                # State machine & agent orchestration
│       │   ├── __init__.py
│       │   ├── agent.py         # StateGraph build & conditional edges
│       │   └── state.py         # MessagesState graph schema
│       │
│       ├── db/                  # Vector Store layer
│       │   ├── __init__.py
│       │   └── vectorstore.py   # FAISS store initialization & embeddings setup
│       │
│       └── tools/               # Agent tool functions
│           ├── __init__.py
│           └── knowledge_tools.py # @tool definitions (vector lookup, document insertion)
│
├── tests/                       # Unit and integration test suites
│   ├── __init__.py
│   └── test_rag_agent.py
│
├── main.py                      # Application CLI entry point
└── evaluate_rag.py              # Automated performance & accuracy benchmark

````

## ⚙️ Core Agent Workflow

The agent operates as a stateful loop managed by LangGraph:

Plaintext

```
    ┌──────────────┐
    │  User Query  │
    └──────┬───────┘
           │
           ▼
┌──────────────────────┐      Calls Tool      ┌──────────────────────┐
│                      ├─────────────────────►│     Tools Node       │
│      LLM Node        │                      │ (e.g., FAISS Search) │
│ (Agent Reasoning)    │◄─────────────────────┤                      │
└──────────┬───────────┘    Returns Context   └──────────────────────┘
           │
           │ Final Answer Generated
           ▼
    ┌──────────────┐
    │    Output    │
    └──────────────┘

```

1. **State Entry:** User query enters the graph wrapped in `HumanMessage`.
2. **LLM Node:** Evaluates chat history and context. Decides whether to issue a tool request (`tool_calls`) or output the final text.
3. **Traffic Control (`tools_condition`):** Routes execution to **Tools Node** if a function call is needed; otherwise routes to **`END`**.
4. **Tools Node:** Executes `@tool` functions (e.g., querying FAISS or adding documents), appends `ToolMessage` back to the state, and routes back to the LLM Node.

## 🚀 Quickstart Guide

### 1. Prerequisites

- Python 3.10+
- Google Gemini API Key

### 2. Environment Setup

Clone the repository and set up a virtual environment:

Bash

```
git clone [https://github.com/maitraria15-dot/enterprise-docsearch-rag.git](https://github.com/maitraria15-dot/enterprise-docsearch-rag.git)
cd enterprise-docsearch-rag

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

```

### 3. Configure Secrets

Create a `.env` file in the project root:

Code snippet

```
GEMINI_API_KEY="your-gemini-api-key-here"
LLM_MODEL_NAME="gemini-2.5-flash"
EMBEDDING_MODEL_NAME="models/text-embedding-004"
FAISS_INDEX_PATH="faiss_index"

```

## 🧪 Testing & Evaluation

Run the automated evaluation suite to benchmark tool routing accuracy, response accuracy, and request latency:

Bash

```
python evaluate_rag.py

```

### Optional: Real-Time Tracing via LangSmith

To enable detailed visual execution traces, set the following in your `.env`:

Code snippet

```
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_API_KEY="your-langsmith-api-key"
LANGCHAIN_PROJECT="enterprise-rag-agent"

```

## 📦 Tech Stack

- **Orchestration:** LangGraph / LangChain
- **LLM Engine:** Google Gemini (`gemini-2.5-flash`)
- **Embedding Model:** Google Gemini Embeddings (`models/text-embedding-004`)
- **Vector Store:** FAISS (`faiss-cpu`)
- **Environment Management:** `python-dotenv`
