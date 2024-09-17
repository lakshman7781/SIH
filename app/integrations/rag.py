import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import requests
import chromadb
from chromadb import HttpClient
from openai import AzureOpenAI
from typing import List, Dict
import textwrap

# Load environment variables
load_dotenv(".env")

# Azure Form Recognizer setup
FORM_RECOGNIZER_ENDPOINT = os.environ["FORM_RECOGNIZER_END_POINT"]
FORM_RECOGNIZER_KEY = os.environ["FORM_RECOGNIZER_KEY"]

# Azure OpenAI setup
OPENAI_API_BASE = os.environ["API_BASE"]
OPENAI_API_KEY = os.environ["API_KEY"]
OPENAI_DEPLOYMENT_NAME = os.environ["DEPLOYMENT_NAME"]
OPENAI_API_VERSION = os.environ["API_VERSION"]

# Initialize clients
document_analysis_client = DocumentAnalysisClient(
    endpoint=FORM_RECOGNIZER_ENDPOINT, credential=AzureKeyCredential(FORM_RECOGNIZER_KEY)
)

chroma_client = HttpClient("http://localhost:6060")
collection_client = chroma_client.get_or_create_collection("RAG")

openai_client = AzureOpenAI(
    api_key=OPENAI_API_KEY,
    api_version=OPENAI_API_VERSION,
    base_url=f"{OPENAI_API_BASE}/openai/deployments/{OPENAI_DEPLOYMENT_NAME}"
)

def extract_text(file_path: str) -> str:
    with open(file_path, "rb") as f:
        poller = document_analysis_client.begin_analyze_document("prebuilt-read", f)
    result = poller.result()
    return result.content

def generate_embeddings(text: str) -> List[float]:
    response = requests.post("http://localhost:6000/generate_embeddings", json={"text": text})
    response.raise_for_status()
    return response.json()

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]:
    chunks = textwrap.wrap(text, chunk_size, break_long_words=False)
    return [chunks[0]] + [chunks[i-1][-overlap:] + chunks[i] for i in range(1, len(chunks))]

def add_document_to_collection(file_path: str, chunks: List[str], embeddings: List[List[float]]):
    ids = [f"{file_path}_{i}" for i in range(len(chunks))]
    collection_client.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
    )
    return f"Document added to collection: {file_path}"

def process_document(file_path: str):
    extracted_text = extract_text(file_path)
    chunks = chunk_text(extracted_text)
    embeddings = [generate_embeddings(chunk) for chunk in chunks]
    return add_document_to_collection(file_path, chunks, embeddings)

def process_documents_in_folder(folder_path: str):
    document_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) 
                      if os.path.isfile(os.path.join(folder_path, file))]
    
    for document_path in document_paths:
        result = process_document(document_path)
        print(result)

def get_chat_completion(prompt: str, context: str) -> str:
    response = openai_client.chat.completions.create(
        model=OPENAI_DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant implementing a RAG model. Answer questions based on the provided context."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {prompt}"}
        ],
    )
    return response.choices[0].message.content

def rag_model(prompt: str, n_results: int = 3) -> Dict[str, str]:
    # Generate embedding for the prompt
    prompt_embedding = generate_embeddings(prompt)
    
    # Retrieve relevant documents
    results = collection_client.query(
        query_embeddings=[prompt_embedding],
        n_results=n_results
    )
    
    # Combine retrieved documents
    context = "\n".join(results['documents'][0])
    
    # Generate response using the context
    response = get_chat_completion(prompt, context)
    
    return {
        "question": prompt,
        "answer": response,
        "context": context
    }

# Example usage
if __name__ == "__main__":
    # Process documents in a folder
    # folder_path = r'path/to/your/documents'
    # process_documents_in_folder(folder_path)
    
    # Use the RAG model
    prompt = "What are the details of Mallikarjuna Reddy Manadi's PAN card?"
    result = rag_model(prompt)
    print(f"Question: {result['question']}")
    print(f"Answer: {result['answer']}")
    print(f"Context used: {result['context']}")