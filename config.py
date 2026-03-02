import os
from dotenv import load_dotenv
import chromadb
from chromadb.utils import embedding_functions

load_dotenv()

class Config:
    HF_TOKEN = os.getenv("HF_TOKEN")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DB_PATH = "./my_rag_database"
    MODEL_HF = 'all-MiniLM-L6-v2'
    MODEL_OAI = "text-embedding-3-small"

client = chromadb.PersistentClient(path=Config.DB_PATH)

# Define both functions
hf_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=Config.MODEL_HF)
oai_ef = embedding_functions.OpenAIEmbeddingFunction(api_key=Config.OPENAI_API_KEY, model_name=Config.MODEL_OAI)