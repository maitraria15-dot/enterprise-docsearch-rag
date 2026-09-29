import os
from dotenv import load_dotenv

load_dotenv(override=True)

class Settings:
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY","")
    LLM_MODEL_NAME: str = os.getenv("LLM_MODEL_NAME","gemini-2.5-flash")
    EMBEDDING_MODEL_NAME: str = os.getenv("EMBEDDING_MODEL_NAME","gemini-embedding-001")
    FAISS_INDEX_PATH: str = os.getenv("FAISS_INDEX_PATH", "faiss_index")

settings = Settings()

