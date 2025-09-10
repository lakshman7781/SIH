import os
from openai import OpenAI
from dotenv import load_dotenv
import json
load_dotenv(".env")

# GitHub OpenAI Models Configuration
token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
chat_model = "openai/gpt-4o"
embedding_model = "openai/text-embedding-3-large"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

def get_chat_completion_openai(prompt: str, text: str):
    response = client.chat.completions.create(
        model=chat_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant in document analysis."},
            {
                "role": "user",
                "content": f"{prompt}\n\nText to analyze: {text}"
            }
        ],
        response_format={"type": "json_object"}
    )
    response_content = response.choices[0].message.content
    response_json = json.loads(response_content)
    return response_json


def get_image_details(images, prompt: str):
    # Note: GitHub OpenAI models may have different image handling capabilities
    # This function may need adjustment based on available models
    messages = [
        {"role": "system", "content": "You are a helpful assistant in document analysis."},
        {"role": "user", "content": prompt}
    ]
    
    # GitHub models may not support image inputs in the same way
    # You may need to adjust this based on available capabilities
    response = client.chat.completions.create(
        model=chat_model,
        messages=messages,
        max_tokens=500
    )
    res = response.choices[0].message.content
    try:
        result = json.loads(res)
    except json.JSONDecodeError:
        result = {"analysis": res}
    return result

def extract_structured_data_with_functions(input_text, function_list, function_call: any = "auto"):
    # GitHub OpenAI models use tools instead of functions (newer API)
    tools = [{"type": "function", "function": func} for func in function_list]
    
    result = client.chat.completions.create(
        model=chat_model,
        messages=[
            {"role": "user", "content": input_text},
        ],
        tools=tools,
        tool_choice=function_call if function_call != "auto" else "auto"
    )
    
    output = result.choices[0].message
    if output.tool_calls:
        details = json.loads(output.tool_calls[0].function.arguments)
        return details
    else:
        # Fallback if no tool calls
        return {"content": output.content}

def get_image_analysis_with_functioncall(images, function_list: list):
    # Note: This may need adjustment based on GitHub model capabilities
    tools = [{"type": "function", "function": func} for func in function_list]
    
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant in document analysis."
        },
        {
            "role": "user",
            "content": "Please analyze the provided images using the available functions."
        }
    ]

    response = client.chat.completions.create(
        model=chat_model,
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    output = response.choices[0].message
    if output.tool_calls:
        result = json.loads(output.tool_calls[0].function.arguments)
        return result
    else:
        return {"content": output.content}

def get_rag_final(prompt: str, context: str) -> str:
    response = client.chat.completions.create(
        model=chat_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant implementing a RAG model who answers in ENGLISH language only. Answer questions based on the provided context."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {prompt}"}
        ],
    )
    response_content = response.choices[0].message.content
    return response_content

def get_embeddings(text):
    """Get embeddings using GitHub OpenAI models"""
    response = client.embeddings.create(
        input=[text],
        model=embedding_model,
    )
    
    # Extract the embedding from the response
    embedding = response.data[0].embedding
    return embedding