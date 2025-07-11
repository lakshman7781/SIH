from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner
from app.workflows.activities.upload import extract_text_from_pdf, extract_structured_data
from app.integrations.function_calls import func_resume_details, get_function_call
from app.integrations.openai import get_chat_completion_openai
from app.integrations.function_calls import DocumentType
from app.integrations.github import get_embeddings
from app.integrations.chromadb import add_embedding_to_collection
from app.constants import document_analysis_prompt
from enum import Enum
import textwrap
from typing import List, Dict




def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]:
    chunks = textwrap.wrap(text, chunk_size, break_long_words=False)
    return [chunks[0]] + [chunks[i-1][-overlap:] + chunks[i] for i in range(1, len(chunks))]


@flow(task_runner=SequentialTaskRunner())
async def document_process_workflow(file_path: str, document_type: DocumentType):
    text = extract_text_from_pdf(file_path)
    function_call = get_function_call(document_type)
    if function_call is not None:
        structured_text = extract_structured_data(input_text=text, function_list=function_call)
        chunks = chunk_text(str(structured_text))
        embeddings = [get_embeddings(chunk) for chunk in chunks] 
        res= add_embedding_to_collection(file_path=file_path, chunks=chunks, embeddings=embeddings, document_type=DocumentType(document_type).name)
        print(res)
        
    else:
        # TODO: implement a long prompt to extract important information from the document that is dependent on the AI
        structured_text=get_chat_completion_openai(prompt=document_analysis_prompt, text=text)
        return structured_text
    return structured_text