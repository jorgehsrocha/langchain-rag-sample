from uuid import uuid4
from langchain_community.document_loaders import PyMuPDFLoader
from models.doc_raw import DocumentRaw
from models.doc_raw_page import DocumentPage

class DocumentExtractor:
    def extract_content(self, file_path: str) -> DocumentRaw:
        """Extracts the content of a document given its file path."""
        if not self.__document_exists(file_path):
            raise FileNotFoundError(f"Document not found: {file_path}")
        loader = PyMuPDFLoader(file_path)

        id = uuid4().hex
        pages = loader.load()
        document = DocumentRaw(id=id, pages=[])
        for page in pages:
            document.pages.append(DocumentPage(
                page_content=page.page_content,
                metadata=page.metadata
            ))
        return document

    def __document_exists(self, file_path: str) -> bool:
        try:
            with open(file_path, 'rb'):
                return True
        except FileNotFoundError:
            return False

        