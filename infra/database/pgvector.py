import os
from infra.embedding import embeddings
from langchain_postgres import PGVector

vector_store = PGVector(
    embeddings=embeddings,
    collection_name=os.environ["PGVECTOR_TABLE_NAME"],
    connection=os.environ["PGVECTOR_URL"],
    use_jsonb=True
)

if not vector_store:
    raise Exception("Database Initialization Error: PGVector store could not be created.")