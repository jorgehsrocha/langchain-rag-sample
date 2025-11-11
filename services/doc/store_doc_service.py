from services.doc.doc_extractor_service import DocumentExtractor
from services.doc.text_splitter_service import TextSplitterService
from services.vector_store.store_vector_service import StoreVectorService


class StoreDocService:
    def __init__(self, path: str):
        self.vector_store_service = StoreVectorService()
        self.extractor = DocumentExtractor()
        self.doc_path = path

    def store(self):
        textSplitter = TextSplitterService(chunk_overlap=500, chunk_size=1500)
        try:
            document = self.extractor.extract_content(self.doc_path)
            existing_docs = self.vector_store_service.fetch_document_by_id(str(document.id))
            if existing_docs:
                print(f"Document {document.id} is already stored. Skipping.")
                return
                
            chunks = []
            for page in document.pages:
                chunks.extend(textSplitter.split_text(page.page_content))

            self.vector_store_service.store_documents([document])
            return document, chunks
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(f"Error processing document: {e}")
            if "CardinalityViolation" in str(e) or "cannot affect row a second time" in str(e):
                try:
                    self.vector_store_service.vector_store.delete(ids=[str(document.id)])
                    self.vector_store_service.store_documents([document])
                except Exception as retry_error:
                    print(f"Failed to store document after cleanup: {retry_error}")
