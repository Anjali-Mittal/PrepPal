import os
import warnings
import logging
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
logging.getLogger('langchain').setLevel(logging.ERROR)
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

load_dotenv()
model_name = os.getenv("EMBEDDING_MODEL")
chroma_db_dir = os.getenv("CHROMA_DB_DIR")

embeddings= SentenceTransformerEmbeddings(model_name=model_name)
vectorstore=Chroma(
    embedding_function=embeddings,
    persist_directory=chroma_db_dir
)

# Query ChromaDB
def retrieve_context(user_query, k=3):
    results=vectorstore.similarity_search(user_query,k=5)
    return results