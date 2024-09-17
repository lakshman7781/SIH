import os
from azure.ai.inference import EmbeddingsClient
from azure.core.credentials import AzureKeyCredential

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