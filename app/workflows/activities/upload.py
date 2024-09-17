from prefect import task
from app.integrations.formrecognizer import extract_text
from app.integrations.openai import extract_structured_data_with_functions
from typing import List, Dict


@task
def extract_text_from_pdf(file_path:str):
    extracted_text= extract_text(file_path)
    return extracted_text

@task
def extract_structured_data(input_text:str,function_list:list):
    structured_data= extract_structured_data_with_functions(input_text=input_text,function_list=function_list)
    return structured_data

