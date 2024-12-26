# DocBot
Design and implement a chatbot system capable of ingesting and interpreting uploaded documents (e.g., PDFs) to provide accurate, fact-based responses quickly and reliably. The chatbot should utilize LLM APIs and other retrieval techniques. 

## TECH STACK
- ChromaDB for vector database storage.
- LangChain for vector store integration.
- Hugging Face Transformers for processing queries.
- Flask for the backend and UI.

## WORK FLOW
- Document Upload:
    - **User Action**: Upload pdf documents via UI
    - **System Action**: Store the uploaded files in vectorized format in chromadb

- Text Extraction and indexing:
    - **System Action**: Extract text from PDF and store it in both locally and in database (sqlite3)
    
- Query Submission:
    - **User action**: User enter the prompt through chatbot UI and call the hugging face api 

- Response Generation and Delivery:
    - **System Action**: Langchain will integrate the api and process the query. It will retrieve the most relevant sections of the document and stream the response through UI.

