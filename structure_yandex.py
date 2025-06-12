import requests
import os
from dotenv import load_dotenv

load_dotenv()

YA_API_KEY = os.getenv("YA_API_KEY")
FOLDER_ID = os.getenv("FOLDER_ID")
IAM_TOKEN = os.getenv("IAM_TOKEN")

def structure_text(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {IAM_TOKEN}"
    }

    body = {
        "modelUri": f"gpt://{FOLDER_ID}/yandexgpt/latest",
        "completionOptions": {
            "stream": False,
            "temperature": 0.3,
            "maxTokens": 700
        },
        "messages": [
            {"role": "user", "text": prompt}
        ]
    }

    response = requests.post(
        url="https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
        headers=headers,
        json=body
    )

    return response.json()
