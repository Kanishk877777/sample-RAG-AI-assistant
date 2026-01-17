import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


def build_chain(retriever):

    llm = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        max_output_tokens=2000,
        temperature=0.5
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a professional legal assistant. Use the provided context to answer accurately. If you don't know the answer, say so."),
        ("user", "Context:\n{context}\n\nQuestion: {question}")
    ])

    chain = (
        {
            "context": retriever | (lambda docs: "\n\n".join(d.page_content for d in docs)),
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
