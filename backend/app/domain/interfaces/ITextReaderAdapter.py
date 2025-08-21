from abc import ABC, abstractmethod
from app.domain.entities.document import Document

class ITextReaderAdapter(ABC):
    @abstractmethod
    def extract_text(self, document: Document) -> str:
        """
        Extracts text from a given document.

        :param document: The document to extract the text from.
        :return: The extracted text.
        """
        pass