from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner
from app.workflows.activities.upload import extract_text_from_pdf, extract_structured_data
from app.integrations.function_calls import func_resume_details

@flow(task_runner=SequentialTaskRunner())
async def data_pipeline(file_path: str):
    text = extract_text_from_pdf(file_path)
    #todo: get function call based on document type
    structured_text = extract_structured_data(input_text=text,function_list=func_resume_details)
    return structured_text