import os
import json
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

# Load environment variables
load_dotenv()
CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR")
model = os.getenv("EMBEDDING_MODEL")

# Load JSON data
def prepare_documents():
    with open("C:/PrepPal/data/subject.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # Convert to Document objects
    documents = []

    for item in data:
        content = item["content"]
        if isinstance(content, list):
            content = "\n".join(content)

        documents.append(
            Document(
                page_content=content,
                metadata={
                    "heading": item["heading"],
                    "subject": item.get("subject", "Unknown")
                }
            )
        )

    # Create embedding model
    embedding_model = SentenceTransformerEmbeddings(model_name=model)

    # Load vectorstore
    vectorstore = Chroma(
        embedding_function=embedding_model,
        persist_directory=CHROMA_DB_DIR
    )

    # Add documents and persist
    vectorstore.add_documents(documents)
    vectorstore.persist()

print("Documents successfully added to Chroma.")

if __name__ == "__main__":
    prepare_documents()