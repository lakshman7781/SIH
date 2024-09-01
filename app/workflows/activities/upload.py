from prefect import task
from app.integrations.formrecognizer import extract_text
from app.integrations.openai import extract_structured_data_with_functions

@task
def extract_text_from_pdf(file_path:str):
    return extract_text(file_path)

@task
def extract_structured_data(input_text:str,function_list:list):
    return extract_structured_data_with_functions(input_text=input_text,function_list=function_list)

