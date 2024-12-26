# from langchain.vectorstores import Chroma
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.schema import Document
# import os

# # Set Hugging Face API token (if needed)
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"  # Replace with your token

# # Initialize ChromaDB and Hugging Face embeddings
# VECTOR_STORE_DIR = "vector_store"
# os.makedirs(VECTOR_STORE_DIR, exist_ok=True)

# embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# vector_store = Chroma(persist_directory=VECTOR_STORE_DIR, embedding_function=embedding_model)

# def add_to_vector_store(doc_id, text):
#     """Add text to the vector store."""
#     doc = Document(page_content=text, metadata={"id": doc_id})
#     vector_store.add_documents([doc])
#     vector_store.persist()

# def retrieve_relevant_content(query):
#     """Retrieve relevant content based on a query."""
#     results = vector_store.similarity_search(query, k=5)  # Retrieve top 5 results
#     if not results:
#         return "No relevant content found."
#     return "\n".join([result.page_content for result in results])



# from langchain.vectorstores import Chroma
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.schema import Document
# import os

# # Set Hugging Face API token (if needed)
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"  # Replace with your token

# # Initialize ChromaDB and Hugging Face embeddings
# VECTOR_STORE_DIR = "vector_store"
# os.makedirs(VECTOR_STORE_DIR, exist_ok=True)

# embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# vector_store = Chroma(persist_directory=VECTOR_STORE_DIR, embedding_function=embedding_model)

# def add_to_vector_store(doc_id, text):
#     """Add text to the vector store."""
#     doc = Document(page_content=text, metadata={"id": doc_id})
#     vector_store.add_documents([doc])
#     vector_store.persist()

# def retrieve_relevant_content(query):
#     """Retrieve relevant content based on a query."""
#     results = vector_store.similarity_search(query, k=5)  # Retrieve top 5 results
#     if not results:
#         return "No relevant content found."
#     return "\n".join([result.page_content for result in results])

from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import os

# Directory for vector store
VECTOR_STORE_DIR = "vector_store"
os.makedirs(VECTOR_STORE_DIR, exist_ok=True)

# Initialize Hugging Face embeddings and ChromaDB
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma(persist_directory=VECTOR_STORE_DIR, embedding_function=embedding_model)

# Text splitter to divide documents into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

def add_to_vector_store(file_path, text):
    """Add extracted text from a file into the vector store."""
    # Split text into smaller chunks
    chunks = text_splitter.split_text(text)
    documents = [Document(page_content=chunk, metadata={"source": file_path}) for chunk in chunks]
    
    # Add documents to vector store and persist
    vector_store.add_documents(documents)
    vector_store.persist()

def retrieve_relevant_content(query):
    """Retrieve precise and relevant content from the vector store."""
    results = vector_store.similarity_search(query, k=3)  # Top 3 results
    if not results:
        return "No relevant content found."
    
    # Combine results into a readable format
    response = "\n\n".join([f"Source: {result.metadata['source']}\nContent: {result.page_content}" for result in results])
    return response


