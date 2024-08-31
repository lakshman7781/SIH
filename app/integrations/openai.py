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


def get_image_details(images, prompt: str):

    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant in document analysis."},
            {"role": "user", "content": [
                {
                    "type": "text",
                    "text": prompt
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{image}"
                    }
                }
                for image in images
            ]}
        ],
        max_tokens=500,
        response_format={"type": "json_object"}
    )
    res= response.choices[0].message.content
    result = json.loads(res)
    return result


def get_image_analysis_with_functioncall(images, function_list: list):
    response = client.chat.completions.create(
        messages=[
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
        ],
        functions=[function_list],
        function_call="auto"
    )

    response = response.choices[0].message
    output = json.loads(response.function_call.arguments)
    return output
