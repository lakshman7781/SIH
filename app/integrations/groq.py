import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv(".env")

api_key=os.environ["GROQ_KEY"]

client = Groq(
    api_key=api_key,
)

def get_chat_completion(prompt: str, text: str):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant in document analysis."},
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
        ],
        model="llama-3.1-8b-instant",
        response_format={"type": "json_object"}  
    )

    return chat_completion.choices[0].message.content

