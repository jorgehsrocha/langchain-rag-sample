import os
from langchain_openai import OpenAIEmbeddings


embedding_model_name = os.environ["OPENAI_EMBEDDING_MODEL_NAME"]

if not embedding_model_name:
    embedding_model_name = "text-embedding-3-small"

embeddings = OpenAIEmbeddings(model=embedding_model_name)