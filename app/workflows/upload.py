from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner
from app.workflows.activities.upload import extract_text_from_pdf, extract_structured_data
from app.integrations.function_calls import func_resume_details, get_function_call
from app.integrations.function_calls import DocumentType
from enum import Enum


@flow(task_runner=SequentialTaskRunner())
async def document_process_workflow(file_path: str, document_type: DocumentType):
    text = extract_text_from_pdf(file_path)
    function_call = get_function_call(document_type)
    if function_call is not None:
        structured_text = extract_structured_data(input_text=text, function_list=function_call)
    else:
        # TODO: implement a long prompt to extract important information from the document that is dependent on the AI
        return "No function call found"
    return structured_text