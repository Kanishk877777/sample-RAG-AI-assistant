from loader import load_docs
from embedding_model import get_embeds
from vector_store import create_vectorstore

docs = load_docs()
embeddings = get_embeds()

create_vectorstore(docs, embeddings)

print("ingestion successful")
