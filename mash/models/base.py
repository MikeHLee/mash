from abc import ABC, abstractmethod
from typing import Generator

class ModelHandler(ABC):
    """Base class for all model handlers"""
    
    @abstractmethod
    def stream_response(self, prompt: str) -> Generator[str, None, None]:
        """Stream the response from the model"""
        pass
