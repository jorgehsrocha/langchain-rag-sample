from langchain_openai import ChatOpenAI
from infra.database.pgvector import vector_store

class AnswerFromDocService:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-5-nano", temperature=0.5)

    def answer_question(self, question: str) -> str:
        stored_response = vector_store.similarity_search(question, k=1)
        content = "\n".join([doc.page_content for doc in stored_response])
        llm_response = self.llm.invoke(
            input = f"""
            QUESTION: {question}
            CONTEXT: {content}
            Provide a concise answer based on the CONTEXT.

            RULES: 
            - ANSWER IN PORTUGUESE
            - If the CONTEXT does not contain relevant information, respond with "Desculpe, não sei a resposta para essa pergunta."
            - Keep the answer brief and to the point.
            -------
            ANSWER:
            """
        )
        return llm_response.text.strip()