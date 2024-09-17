import chromadb
from chromadb import HttpClient
chroma_client = HttpClient("http://localhost:8000")
collection_client = chroma_client.get_or_create_collection("SIH")

def add_document_to_collection(file_path,extracted_text,embeddings,document_type):
    flattened_metadata = {
        "document_type": document_type
    }
    collection_client.add(
        ids=[file_path],
        documents=[extracted_text],
        embeddings=[embeddings],
        metadatas=[flattened_metadata]
    )
    return "Document added to collection"
