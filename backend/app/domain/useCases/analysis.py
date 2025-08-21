from typing import Optional
from app.domain.entities.document import Document
from app.domain.interfaces.ITextReaderAdapter import ITextReaderAdapter
from app.domain.interfaces.INLPAdapter import INLPAdapter

class AnalysisUseCase:

    def __init__(self, text_reader_adapter: ITextReaderAdapter, nlp_adapter: INLPAdapter):
        self.text_reader_adapter = text_reader_adapter
        self.nlp_adapter = nlp_adapter

    async def execute(self, file: Optional[bytes] = None, text: Optional[str] = None) -> None:
        file_bytes = await file.read() if file else None
        document = Document(
            filename=file.filename if file else None,
            size=file.size if file else None,
            content=file_bytes,
            text=text
        )
        raw_text = self.text_reader_adapter.extract_text(document)
        print("raw_text",raw_text)