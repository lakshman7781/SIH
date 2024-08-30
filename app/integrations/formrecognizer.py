from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import os

endpoint = os.environ.get['FORM_RECOGNIZER_END_POINT']
key = os.environ.get["FORM_RECOGNIZER_KEY"]


def extract_text(file_path:str):

    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )
    
    poller = document_analysis_client.begin_analyze_document_from_url(
            "prebuilt-read", file_path)
    result = poller.result()

    print ("Document contains content: ", result.content)
    