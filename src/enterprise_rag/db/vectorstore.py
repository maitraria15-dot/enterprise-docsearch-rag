from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from enterprise_rag.config import settings
EMBEDDING_MODEL_NAME = "gemini-embedding-001"
class VectorStoreManager:
    def __init__(self):
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model = settings.EMBEDDING_MODEL_NAME,
            google_api_key = settings.GOOGLE_API_KEY
        )
        self.vector_store = FAISS.from_texts(
            texts = ["Initial knowledge base seed."],
            embedding=self.embeddings,
            metadatas=[{"source": "system_init"}]
        )

    def search(self, query: str, k: int = 3) -> str:
        results = self.vector_store.similarity_search(query, k=k)
        if not results:
            return "No relevant internal documents found."
        return "\n\n".join(
            [f"[Source: {doc.metadatas.get('source', 'Unknown')}]\n{doc.page_content}" for doc in results]
        )
    def add_document(self, content: str, source_name: str) -> str:
        self.vector_store.add_texts(
            texts = [content],
            metadatas = [{"source": source_name}]
        )
        return f"Successfully ingestd document '{source_name}' into knowledge base."

vector_manager = VectorStoreManager()