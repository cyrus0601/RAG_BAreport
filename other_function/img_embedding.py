"""
Description: This script is used to convert image to base64 format to ask LLM
"""
# %%
import os
import base64
import io

from openai import AzureOpenAI
from PIL import Image

# %%
os.environ["AZURE_OPENAI_API_KEY"] = ""
os.environ["AZURE_OPENAI_API_VERSION"] = ""
os.environ["AZURE_OPENAI_ENDPOINT"] = ""

print("AZURE_OPENAI_API_KEY:", os.getenv("AZURE_OPENAI_API_KEY"))
print("AZURE_OPENAI_API_VERSION:", os.getenv("AZURE_OPENAI_API_VERSION"))
print("AZURE_OPENAI_ENDPOINT:", os.getenv("AZURE_OPENAI_ENDPOINT"))

# %%
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  
image_path = "output_image.png"
base64_image = encode_image(image_path)


# %%
client = AzureOpenAI(
      azure_endpoint = "", 
      api_key=os.environ[""],  
      api_version=""
    )

# %%
response = client.chat.completions.create(
        model="gpt4-o", 
        messages=[
            {   
                "system": "你是一個繁體中文AI助理，可以完成使用者交派給你的任務。",
                "role": "user",
                "content": [
                    {"type": "text", "text": ""},
                    {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image}"
                    },
                    },
                ],
            }
        ],
        stream=True,
    )


# %%
for chunk in response:
    if chunk.choices:
        first_choice = chunk.choices[0]
        if first_choice.delta and first_choice.delta.content is not None:
            print(first_choice.delta.content, end="", flush=True) 


