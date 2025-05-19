import requests
from typing import Optional

class GPT4Interface:
    """
    Simple interface for interacting with OpenAI GPT-4 API.
    """
    def __init__(self, api_key: str, api_url: Optional[str] = None):
        self.api_key = api_key
        self.api_url = api_url or "https://api.openai.com/v1/chat/completions"

    def ask(self, prompt: str, model: str = "gpt-4", max_tokens: int = 512, temperature: float = 0.7) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": max_tokens,
            "temperature": temperature
        }
        response = requests.post(self.api_url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip() 