from .base import ModelHandler
from .openai_handler import OpenAIHandler
from .anthropic_handler import AnthropicHandler
from .ollama_handler import OllamaHandler

def get_model_handler(model_name: str) -> ModelHandler:
    """Factory function to get the appropriate model handler"""
    handlers = {
        'gpt4': OpenAIHandler,
        'claude': AnthropicHandler,
        'ollama': OllamaHandler
    }
    
    if model_name not in handlers:
        raise ValueError(f"Unknown model: {model_name}")
    
    return handlers[model_name]()
