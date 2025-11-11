from pydantic import BaseModel

class DocumentPage(BaseModel):
    page_content: str
    metadata: dict
    page_number: int | None = 0