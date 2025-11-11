import dotenv
dotenv.load_dotenv()

from services.doc.answer_from_doc import AnswerFromDocService
from services.doc.store_doc_service import StoreDocService

answer_service = AnswerFromDocService()


def load_document():
    try:
        file_path = "sample.pdf"
        storeDocService = StoreDocService(file_path)
        doc_stored = storeDocService.store()
        if not doc_stored:
            print("Document was not stored.")
    except FileNotFoundError as e:
        print("File not found:", e)
    except Exception as e:
        print(f"Error processing document: {e}")

def make_question():
    input_from = input("PERGUNTA: ")
    answer = answer_service.answer_question(input_from)
    print("RESPOSTA: ", answer)
    print("========"*10)
    return make_question()

if __name__ == "__main__":
    print("========"*10)
    load_document()
    make_question()