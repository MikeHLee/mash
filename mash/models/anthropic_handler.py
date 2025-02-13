from typing import Generator
import anthropic
from .base import ModelHandler
from . import secrets
from .anthropic import configs

class AnthropicHandler(ModelHandler):
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=secrets.ANTHROPIC_API_KEY)
        self.config = configs.DEFAULT_CONFIG
    
    def stream_response(self, prompt: str) -> Generator[str, None, None]:
        try:
            with self.client.messages.stream(
                model=self.config["model"],
                messages=[{"role": "user", "content": prompt}],
                **self.config["parameters"]
            ) as stream:
                for text in stream.text_stream:
                    yield text
                    
        except Exception as e:
            raise Exception(f"Anthropic API error: {str(e)}")
