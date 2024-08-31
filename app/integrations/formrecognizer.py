from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import os
from dotenv import load_dotenv
load_dotenv(".env")

endpoint = os.environ["FORM_RECOGNIZER_END_POINT"]
key = os.environ["FORM_RECOGNIZER_KEY"]


def extract_text(file_path:str):

    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint,credential=AzureKeyCredential(key)
    )
    
    with open(file_path, "rb") as f:
        poller = document_analysis_client.begin_analyze_document("prebuilt-read", f)
    result = poller.result()

    print ("Document contains content: ", result.content)
    