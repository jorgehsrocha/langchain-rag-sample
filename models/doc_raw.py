from pydantic import BaseModel
from models.doc_raw_page import DocumentPage

class DocumentRaw(BaseModel):
    id: str
    pages: list[DocumentPage] = []
