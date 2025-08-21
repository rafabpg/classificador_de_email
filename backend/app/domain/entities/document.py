from enum import Enum
from typing import Optional

class FileType(str, Enum):
    TXT = "txt"
    PDF = "pdf"

MAX_FILE_SIZE = 10 * 1024 * 1024 # 10 MB

class Document:
    def __init__(
    
        self,
        filename: Optional[str] = None,
        size: Optional[int] = None,
        content: Optional[bytes] = None,
        text: Optional[str] = None,
    ): 
        """
        Initializes a Document instance.

        Args:
            filename (Optional[str]): The name of the file associated with the document. Must have a supported extension (PDF or TXT).
            size (Optional[int]): The size of the file in bytes. Must not exceed MAX_FILE_SIZE (10 MB).
            content (Optional[bytes]): The binary content of the file.
            text (Optional[str]): The textual content of the document.

        Raises:
            ValueError: If neither filename nor text is provided.
            ValueError: If the file size exceeds the maximum allowed size.
            ValueError: If the file extension is not supported.

        Notes:
            Either a file (PDF or TXT) or text must be provided to create a Document.
        """
        if not filename and not text:
            raise ValueError("Um documento deve ter um arquivo pdf ou um texto.")
        if size is not None and size > MAX_FILE_SIZE:
            raise ValueError("O tamanho do arquivo não pode ser maior que 10 MB.")
        self.filename = filename
        self.content = content
        self.text = text
        self.filetype: Optional[FileType] = None

        if filename:
            ext = filename.split(".")[-1].lower()
            if ext not in (FileType.TXT, FileType.PDF):
                raise ValueError(f"Formato de arquivo não suportado: {ext}")
            self.filetype = FileType(ext)