from typing import Optional
from app.domain.entities.document import Document
from app.domain.interfaces.ITextReaderAdapter import ITextReaderAdapter
from app.domain.interfaces.INLPAdapter import INLPAdapter
from app.domain.interfaces.IEmailAnalyzer import IEmailAnalyzer
from app.api.schemas.responses import AnalysisResponse

class AnalysisUseCase:

    def __init__(self, text_reader_adapter: ITextReaderAdapter, nlp_adapter: INLPAdapter, email_analyzer: IEmailAnalyzer):
        """
        Initialize the AnalysisUseCase.

        Args:
            text_reader_adapter (ITextReaderAdapter): The adapter to read text from a document.
            nlp_adapter (INLPAdapter): The adapter to perform NLP analysis on a text.
            email_analyzer (IEmailAnalyzer): The adapter to analyze an email.
        """
        self.text_reader_adapter = text_reader_adapter
        self.nlp_adapter = nlp_adapter
        self.email_analyzer = email_analyzer

    async def execute(self, file: Optional[bytes] = None, text: Optional[str] = None) -> dict:
        """
        Perform an analysis on a given file or text.

        Args:
            file (Optional[bytes]): The file to be analyzed. Defaults to None.
            text (Optional[str]): The text to be analyzed. Defaults to None.

        Returns:
            dict: A dictionary containing the analysis result and details.
        """
        file_bytes = await file.read() if file else None
        document = Document(
            filename=file.filename if file else None,
            size=file.size if file else None,
            content=file_bytes,
            text=text
        )
        raw_text = self.text_reader_adapter.extract_text(document)
        processed_text = self.nlp_adapter.preprocess(raw_text)
        classification_result, details = await self.email_analyzer.analyse_email(processed_text)
        return AnalysisResponse(
            category=classification_result,
            details=details
        )