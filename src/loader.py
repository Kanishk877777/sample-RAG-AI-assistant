from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

def load_docs():
    loader = DirectoryLoader(
        path='data/raw_docs',
        glob='*.pdf',
        loader_cls=PyPDFLoader
    )
    return loader.load()