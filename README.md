# Document Ingestion and Search System

A RAG (Retrieval-Augmented Generation) system built with LangChain for document ingestion, vector storage, and intelligent question answering.

## Features

- PDF document processing and text extraction
- Vector embeddings generation using OpenAI
- PostgreSQL with pgvector for vector storage
- Intelligent document-based question answering
- Text chunking and splitting for optimal retrieval

## Tech Stack

- **Python 3.9+**
- **LangChain** - Document processing and RAG pipeline
- **PostgreSQL + pgvector** - Vector database
- **OpenAI** - Embeddings and language model
- **Docker** - Database containerization

## Project Structure

```
├── main.py                 # Main application entry point
├── docker-compose.yaml     # PostgreSQL with pgvector setup
├── requirements.txt        # Python dependencies
├── sample.pdf             # Sample document for testing
├── infra/
│   ├── database/          # Database connection setup
│   └── embedding.py       # Embedding configuration
├── models/                # Data models
│   ├── doc_raw.py
│   └── doc_raw_page.py
├── repo/                  # Repository layer
│   └── document.py
└── services/
    ├── doc/               # Document processing services
    │   ├── answer_from_doc.py
    │   ├── doc_extractor_service.py
    │   ├── store_doc_service.py
    │   └── text_splitter_service.py
    └── vector_store/      # Vector storage services
        ├── search-vector-service.py
        └── store_vector_service.py
```

## Setup

### Prerequisites

- Python 3.9+
- Docker and Docker Compose
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your OpenAI API key and database settings
```

5. Start PostgreSQL with pgvector:
```bash
docker-compose up -d
```

## Usage

### Running the Application

```bash
python main.py
```

The application will:
1. Load and process the sample PDF document
2. Generate embeddings and store them in the vector database
3. Start an interactive Q&A session

### Adding New Documents

Replace `sample.pdf` with your document or modify the `file_path` in `main.py`:

```python
file_path = "your-document.pdf"
```

### Environment Variables

Create a `.env` file with:

```env
OPENAI_API_KEY=your_openai_api_key_here
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/rag
```

## Architecture

The system follows a layered architecture:

1. **Document Processing**: Extracts text from PDFs and splits into chunks
2. **Embedding Generation**: Creates vector embeddings using OpenAI
3. **Vector Storage**: Stores embeddings in PostgreSQL with pgvector
4. **Retrieval**: Searches for relevant document chunks
5. **Generation**: Uses LLM to generate answers based on retrieved context

## Dependencies

- `langchain_community` - Community integrations
- `langchain_core` - Core LangChain functionality
- `langchain_openai` - OpenAI integration
- `langchain_postgres` - PostgreSQL vector store
- `langchain_text_splitters` - Text chunking utilities
- `pydantic` - Data validation
- `python-dotenv` - Environment variable management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.
