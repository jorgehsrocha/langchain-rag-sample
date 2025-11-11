from infra.database.pgvector import vector_store

class SearchVectorService:
    def __init__(self):
        self.vector_store = vector_store

    def search(self, query, k=5):
        """Searches the vector store for similar documents to the query."""
        return self.vector_store.similarity_search(query, k=k)