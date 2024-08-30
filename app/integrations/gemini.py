import google.ai.generativelanguage as glm
import google.generativeai as genai
import PIL.Image
import base64
import io
import os

api_key=os.environ.get["GEMINI_KEY"]

genai.configure(api_key=api_key)

def image_extraction(images, input_text: str):
        images_list = []
        for image in images:
            img = PIL.Image.open(io.BytesIO(base64.b64decode(image)))
            images_list.append(img)
        images_list.append(input_text)
        model = genai.GenerativeModel('gemini-1.5-flash',
                                      generation_config={
                                          "temperature": 0.0,
                                          "top_p": 1,
                                          "max_output_tokens": 2048,
                                      },)
        
        result = model.generate_content(images_list)
        output = result.candidates[0].content.parts[0].text
        return output