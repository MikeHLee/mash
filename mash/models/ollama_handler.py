from typing import Generator
import requests
from .base import ModelHandler
from .ollama import configs

class OllamaHandler(ModelHandler):
    def __init__(self):
        self.base_url = "http://localhost:11434/api"
        self.config = configs.DEFAULT_CONFIG
    
    def stream_response(self, prompt: str) -> Generator[str, None, None]:
        try:
            response = requests.post(
                f"{self.base_url}/generate",
                json={
                    "model": self.config["model"],
                    "prompt": prompt,
                    "stream": True,
                    **self.config["parameters"]
                },
                stream=True
            )
            response.raise_for_status()
            
            for line in response.iter_lines():
                if line:
                    # Parse the JSON response and extract the text
                    chunk = requests.json().loads(line)
                    if "response" in chunk:
                        yield chunk["response"]
                        
        except Exception as e:
            raise Exception(f"Ollama API error: {str(e)}")
