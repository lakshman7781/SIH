import chromadb
from chromadb import HttpClient
from typing import List, Dict
from azure.ai.inference import EmbeddingsClient
from azure.core.credentials import AzureKeyCredential

chroma_client = HttpClient("http://chroma:8000")
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

def add_embedding_to_collection(file_path: str, chunks: List[str], embeddings: List[List[float]],document_type: str):
    ids = [f"{file_path}_{i}" for i in range(len(chunks))]
    metadatas = [{"document_type": document_type} for _ in range(len(chunks))]

    collection_client.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )
    return f"Document added to collection: {file_path}"

def get_embeddings(text):
    endpoint = "https://models.inference.ai.azure.com"
    model_name = "text-embedding-3-large"
    token = "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"

    client = EmbeddingsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token)
    )

    response = client.embed(
        input=[text],
        model=model_name
    )

    # Flatten the embeddings
    embeddings = [item for sublist in [item.embedding for item in response.data] for item in sublist]
    return embeddings


def rag_model(document_type:str, prompt: str, n_results: int = 10) -> Dict[str, str]:
    # Append additional instructions to the prompt
    # Generate embedding for the prompt
    prompt_embedding = get_embeddings(prompt)
    
    # Retrieve relevant documents
    results = collection_client.query(
        query_embeddings=[prompt_embedding],
        n_results=n_results,
        where={"document_type": {"$ne": document_type}}
    )
    
    # Combine retrieved documents
    context = "\n".join(results['documents'][0])
    return context