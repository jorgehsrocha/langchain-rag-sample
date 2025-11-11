import uuid
from infra.database.pgvector import vector_store
from models.doc_raw import DocumentRaw
from langchain_core.documents import Document

class StoreVectorService:
    def __init__(self):
        self.vector_store = vector_store

    def fetch_document_by_id(self, document_id: str):
        try:
            results = self.vector_store.similarity_search(
                query="", 
                k=1, 
                filter={"document_id": document_id}
            )
            return results
        except Exception:
            try:
                return self.vector_store.get_by_ids([document_id])
            except Exception:
                return []

    def store_text(self, vectors: list[str]):
        unique_id = uuid.uuid4()
        self.vector_store.add_texts(
            texts=vectors,
            metadatas=[{"id": unique_id} for _ in vectors],
            ids=[f"{unique_id}-{i}" for i in range(len(vectors))]
        )
    
    def store_documents(self, documents: list[DocumentRaw]):
        if not documents or len(documents) == 0:
            print("No documents to store.")
            return

        for doc in documents:
            if not doc.pages or len(doc.pages) == 0:
                print(f"Document {doc.id} has no pages.")
                continue
            try:
                existing_docs = self.vector_store.similarity_search(
                    query="", 
                    k=1, 
                    filter={"document_id": str(doc.id)}
                )
                if existing_docs:
                    print(f"Document {doc.id} is already stored. Skipping.")
                    continue
            except Exception:
                pass

            vector_entries = []
            for page in doc.pages:
                unique_id = str(uuid.uuid4())
                vector_entries.append(
                    Document(
                        page_content=page.page_content,
                        metadata={
                            **page.metadata,
                            "document_id": str(doc.id),
                            "page_number": page.page_number,
                            "unique_id": unique_id
                        }
                    )
                )
            
            if vector_entries:
                try:
                    ids = [str(uuid.uuid4()) for _ in vector_entries]
                    self.vector_store.add_documents(vector_entries, ids=ids)
                except Exception as e:
                    print(f"Error storing document {doc.id}: {e}")
                    raise