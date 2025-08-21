import io
from PyPDF2 import PdfReader
from app.domain.entities.document import Document, FileType
from app.domain.interfaces.ITextReaderAdapter import ITextReaderAdapter

class TextReaderAdapter(ITextReaderAdapter):
    def extract_text(self, document: Document) -> str:
        if document.text:  
            return document.text

        if document.filetype == FileType.TXT:
            return self._extract_from_txt(document.content)

        if document.filetype == FileType.PDF:
            return self._extract_from_pdf(document.content)
    
        raise ValueError("Tipo de arquivo não suportado para extração de texto.")

    def _extract_from_txt(self, content: bytes) -> str:
        """
        Extracts and decodes text content from a bytes object, attempting UTF-8 decoding first.
        If UTF-8 decoding fails due to a UnicodeDecodeError, falls back to ISO-8859-1 decoding,
        ignoring any errors encountered during decoding.

        Args:
            content (bytes): The raw bytes content to be decoded.

        Returns:
            str: The decoded and stripped text content.
        """
        try:
            return content.decode('utf-8').strip()
        except UnicodeDecodeError:
            return content.decode("iso-8859-1", errors="ignore")

    def _extract_from_pdf(self, content: bytes) -> str:
        """
        Extracts text content from a PDF file in bytes format.

        The text is extracted from each page of the PDF and concatenated with newline characters.
        If the PDF does not contain any extractable text, a ValueError is raised.

        Args:
            content (bytes): The raw bytes content of the PDF file.

        Returns:
            str: The extracted text content from the PDF file.

        Raises:
            ValueError: If the PDF does not contain any extractable text or if an error occurs while reading the PDF.
        """
        try:
            pdf_stream = io.BytesIO(content)
            reader = PdfReader(pdf_stream)

            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            if not text.strip():
                raise ValueError("O PDF não contém texto extraível")
            return text.strip()
        except Exception as e:
            raise ValueError(f"Erro ao ler PDF: {e}")