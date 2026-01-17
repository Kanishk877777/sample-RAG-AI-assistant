from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

CHROMA_PATH = "chroma_db"


def create_vectorstore(docs, embeddings):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )
    chunks = splitter.split_documents(docs)

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )
    return db


def load_vectorstore(embeddings):
    return Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )
