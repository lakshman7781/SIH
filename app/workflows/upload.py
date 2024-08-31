from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner
from app.workflows.activities.upload import extract_text_from_pdf

@flow(task_runner=SequentialTaskRunner())
async def data_pipeline(file_path: str):
    return extract_text_from_pdf(file_path)