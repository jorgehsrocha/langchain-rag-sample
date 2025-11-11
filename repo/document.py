from infra.database.pgvector import vector_store


class DocumentRepository:
    def __init__(self):
        self.vector_store = vector_store

    def save_document(self, id: str, content: str, metadata: dict):
        self.vector_store.add_texts(
            texts=[content],
            metadatas=[metadata],
            ids=[id]
        )