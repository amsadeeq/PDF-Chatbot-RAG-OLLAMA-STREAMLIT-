# PDF Chatbot with RAG, OLLAMA & STREAMLIT

A powerful interactive chatbot application that leverages Retrieval-Augmented Generation (RAG) to answer questions based on PDF documents. Built with OLLAMA for local LLM inference and STREAMLIT for an intuitive user interface.

## 🚀 Overview

This project implements an intelligent chatbot that can read and understand PDF documents, then answer user questions based on the content. It combines:

- **OLLAMA**: For running large language models locally without external API calls
- **RAG (Retrieval-Augmented Generation)**: To ground responses in actual document content
- **STREAMLIT**: For a user-friendly web-based interface
- **Vector Database**: For efficient document embedding and retrieval

## ✨ Key Features

- 📄 **PDF Upload & Processing**: Upload multiple PDF files for the chatbot to learn from
- 🤖 **Local LLM**: Run language models locally using OLLAMA
- 🔍 **Context-Aware Responses**: Get answers grounded in document content using RAG
- 💬 **Interactive Chat Interface**: Beautiful, responsive web UI built with STREAMLIT
- 🧠 **Vector Embeddings**: Efficient similarity-based document retrieval
- ⚡ **Real-Time Processing**: Instant responses with relevant context

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- OLLAMA (Download from [ollama.ai](https://ollama.ai))
- pip (Python package manager)

## 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/amsadeeq/PDF-Chatbot-RAG-OLLAMA-STREAMLIT-.git
   cd PDF-Chatbot-RAG-OLLAMA-STREAMLIT-
   ```

2. **Install OLLAMA**
   - Visit [ollama.ai](https://ollama.ai) and download the installer for your OS
   - Follow the installation instructions
   - Verify installation: `ollama --version`

3. **Create a Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Dependencies

The project uses the following Python libraries:

- **streamlit**: Web application framework
- **PyPDF2**: PDF text extraction
- **langchain**: Framework for building LLM applications
- **ollama**: Python client for OLLAMA
- **numpy**: Numerical computations
- **python-dotenv**: Environment variable management

See `requirements.txt` for complete list and versions.

## 🚀 Getting Started

1. **Pull an OLLAMA Model**  
   First, pull a language model using OLLAMA:
   ```bash
   ollama pull mistral  # or llama2, neural-chat, etc.
   ollama serve         # Start OLLAMA server (keep this running)
   ```

2. **Run the Application**  
   In a new terminal, execute:
   ```bash
   streamlit run app.py
   ```

3. **Access the Web Interface**  
   The application will open automatically in your browser at `http://localhost:8501`

## 📖 Usage

1. **Upload PDF Files**
   - Click the file uploader in the sidebar
   - Select one or multiple PDF files
   - Wait for processing to complete (embeddings will be generated)

2. **Ask Questions**
   - Type your question in the chat input
   - The chatbot will search relevant document sections
   - Get AI-generated answers based on document content

3. **View History**
   - Chat history is maintained throughout the session
   - References to source documents are provided

## 📁 Project Structure

```
PDF-Chatbot-RAG-OLLAMA-STREAMLIT-/
├── app.py                          # Main STREAMLIT application
├── requirements.txt                 # Python dependencies
├── pdfs/                           # Directory for PDF files
├��─ uploads/                        # Directory for uploaded PDFs
├── vector_db/                      # Vector database storage
├── Air_India(RAG Chatbot).ipynb   # Jupyter notebook with examples
├── 1.pdf                           # Sample PDF file
└── Screenshots/                    # Application screenshots
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root (optional):

```
OLLAMA_MODEL=mistral
OLLAMA_BASE_URL=http://localhost:11434
CHUNK_SIZE=500
CHUNK_OVERLAP=50
```

### Supported OLLAMA Models

- `mistral` (Fast, good quality)
- `llama2` (Powerful, more resources)
- `neural-chat` (Optimized for chat)
- `dolphin-mixtral` (Advanced)

## 🔄 How It Works

```
1. PDF Upload
   ↓
2. Text Extraction & Chunking
   ↓
3. Generate Embeddings
   ↓
4. Store in Vector Database
   ↓
5. User Question
   ↓
6. Query Vector Database (Similarity Search)
   ↓
7. Retrieve Relevant Chunks
   ↓
8. Pass to OLLAMA with Context
   ↓
9. Generate Response
   ↓
10. Display in Chat Interface
```

## 🖼️ Screenshots

The application includes sample screenshots showing:
- PDF upload interface
- Chat interaction examples
- Real-time response generation

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Troubleshooting

### OLLAMA Connection Issues
- Ensure OLLAMA server is running: `ollama serve`
- Check if OLLAMA is accessible at `http://localhost:11434`

### Out of Memory Errors
- Use a smaller model (e.g., `mistral` instead of `llama2`)
- Reduce `CHUNK_SIZE` in configuration
- Limit number of PDFs processed at once

### Slow Response Times
- Check system resources (CPU/RAM/GPU)
- Ensure PDF files are not too large
- Consider using a faster model

### PDF Parsing Issues
- Verify PDF files are not corrupted
- Ensure PDFs contain extractable text (not scanned images)
- Try re-uploading the file

## 📚 Resources

- [OLLAMA Documentation](https://ollama.ai/docs)
- [STREAMLIT Documentation](https://docs.streamlit.io/)
- [LangChain Documentation](https://python.langchain.com/)
- [RAG Concept Guide](https://python.langchain.com/docs/use_cases/question_answering/)

## ❓ FAQ

**Q: Can I use GPU acceleration?**
A: Yes! OLLAMA automatically detects and uses GPU if available.

**Q: How many PDFs can I upload?**
A: Limited by available system memory. Start with 5-10 PDFs for testing.

**Q: Can I use different LLMs?**
A: Yes! OLLAMA supports many models. Check available options with `ollama list`.

**Q: Is my data private?**
A: Yes! Everything runs locally. No data is sent to external servers.

## 👨‍💻 Author

**Amsadeeq** - [GitHub Profile](https://github.com/amsadeeq)

## 🙏 Acknowledgments

- OLLAMA for local LLM capabilities
- STREAMLIT for the excellent UI framework
- LangChain for RAG implementation support
- The open-source community

---

**Last Updated**: 2026-03-14 07:49:58

For issues, questions, or suggestions, please open an issue on GitHub.