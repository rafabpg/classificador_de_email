from abc import ABC, abstractmethod

class INLPAdapter(ABC):

    @abstractmethod
    def preprocess(self, text: str) -> str:
        pass