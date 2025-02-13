from typing import Generator
import openai
from .base import ModelHandler
from . import secrets
from .openai import configs

class OpenAIHandler(ModelHandler):
    def __init__(self):
        openai.api_key = secrets.OPENAI_API_KEY
        self.config = configs.DEFAULT_CONFIG
    
    def stream_response(self, prompt: str) -> Generator[str, None, None]:
        try:
            response = openai.chat.completions.create(
                model=self.config["model"],
                messages=[{"role": "user", "content": prompt}],
                stream=True,
                **self.config["parameters"]
            )
            
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content
                    
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")
