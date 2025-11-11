from typing import Iterable
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

class TextSplitterService:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def split_text(self, text: str) -> list[str]:
        self.text_splitter.split_documents
        return self.text_splitter.split_text(text)

    def split_documents(self, documents: Iterable[Document]) -> list[Document]:
        return self.text_splitter.split_documents(documents)