from openai.lib.azure import AzureOpenAI
from dotenv import load_dotenv
import os
import json
load_dotenv(".env")

api_base = os.environ["API_BASE"]
api_key = os.environ["API_KEY"]
deployment_name = os.environ["DEPLOYMENT_NAME"]
api_version = os.environ["API_VERSION"]

client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    base_url=f"{api_base}/openai/deployments/{deployment_name}"
)

def get_chat_completion_openai(prompt: str, text: str):
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant in document analysis which returns the extracted text in json format remove ' ```json 'in starting and ending while returning."},
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "text",
                        "text": text
                    }
                ]
            }
        ]
    )
    return response.choices[0].message.content


def get_image_details(images, prompt: str):
    messages = [
        {"role": "system", "content": "You are a helpful assistant in document analysis."},
        {"role": "user", "content": [
            {
                "type": "text",
                "text": prompt
            }
        ]}
    ]
    
    for image in images:
        messages.append(
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{image}"
                }
            }
        )

    response = client.chat.completions.create(
        model=deployment_name,
        messages=messages,
        max_tokens=500,
        response_format="json"
    )
    res = response.choices[0].message.content
    result = json.loads(res)
    return result

def extract_structured_data_with_functions(input_text, function_list, function_call: any = "auto"):
        result = client.chat.completions.create(
            model=deployment_name,
            n=1,
            temperature=0.0,
            messages=[
                {"role": "user", "content": input_text},
            ],
            functions=[function_list],
            function_call=function_call  
        )
        output = result.choices[0].message
        details = json.loads(output.function_call.arguments)
        return details

def get_image_analysis_with_functioncall(images, function_list: list):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant in document analysis."
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{image}"
                    }
                }
                for image in images
            ]
        }
    ]

    response = client.chat.completions.create(
        model=deployment_name,
        messages=messages,
        functions=function_list,
        function_call="auto"
    )

    response = response.choices[0].message
    output = json.loads(response.function_call.arguments)
    return output