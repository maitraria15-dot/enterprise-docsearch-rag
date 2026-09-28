from langchain_core.tools import tool
from enterprise_rag.db.vectorstore import vector_manager

@tool
def search_internal_knowledge(query: str) -> str:
    """Searches the company internal document vector store for relevant knowledge."""
    return vector_manager(query)

@tool
def add_document_to_knowledge_base(content: str, source_name: str) -> str:
    """Adds a new text snippet or document entry into the internal knowledge base."""
    return vector_manager.add_document(content, source_name)

tools = [search_internal_knowledge, add_document_to_knowledge_base]
