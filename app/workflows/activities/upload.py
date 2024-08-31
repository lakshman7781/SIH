from prefect import task
from app.integrations.formrecognizer import extract_text

@task
def extract_text_from_pdf(file_path:str):
    return extract_text(file_path)

