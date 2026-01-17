from src.embedding_model import get_embeds
from src.vector_store import load_vectorstore
from src.chain import build_chain


def ask_legal_question(question):
    try:
        embeddings = get_embeds()
        vectorstore = load_vectorstore(embeddings)
        retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

        chain = build_chain(retriever)

        result = chain.invoke(question)
        return str(result).strip()
    except Exception as e:
        print(f"Error occurred: {e}")
        return "An error occurred while processing your request."
