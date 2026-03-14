import os
import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings

from langchain_ollama import ChatOllama


# -----------------------
# CONFIG
# -----------------------

UPLOAD_DIR = "uploads"
VECTOR_DIR = "vector_db"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(VECTOR_DIR, exist_ok=True)

st.set_page_config(
    page_title="Abubakar AI PDF Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Abubakar AI Document Assistant")

# -----------------------
# LOAD MODELS
# -----------------------

llm = ChatOllama(model="llama3.2:latest")
embeddings = OllamaEmbeddings(model="nomic-embed-text")


# -----------------------
# SIDEBAR
# -----------------------

st.sidebar.title("📂 Document Manager")

uploaded_files = st.sidebar.file_uploader(
    "Upload PDFs",
    type="pdf",
    accept_multiple_files=True
)

# Save uploaded files
if uploaded_files:
    for file in uploaded_files:
        path = os.path.join(UPLOAD_DIR, file.name)
        with open(path, "wb") as f:
            f.write(file.getbuffer())

    st.sidebar.success("Files uploaded successfully")


# -----------------------
# DOCUMENT INDEXING
# -----------------------

def index_documents():

    docs = []

    for file in os.listdir(UPLOAD_DIR):

        if file.endswith(".pdf"):

            loader = PyPDFLoader(os.path.join(UPLOAD_DIR, file))
            docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    vectordb = FAISS.from_documents(chunks, embeddings)

    vectordb.save_local(VECTOR_DIR)

    return len(chunks)


if st.sidebar.button("⚡ Index Documents"):

    with st.spinner("Indexing documents..."):

        total_chunks = index_documents()

    st.sidebar.success(f"{total_chunks} chunks indexed")


# -----------------------
# LOAD VECTOR DB
# -----------------------

def load_vector_db():

    if os.path.exists(VECTOR_DIR):

        return FAISS.load_local(
            VECTOR_DIR,
            embeddings,
            allow_dangerous_deserialization=True
        )

    return None


vectordb = load_vector_db()
if vectordb is None:
    st.info("📂 Upload PDFs and click **Index Documents** to start chatting.")

# -----------------------
# CHAT HISTORY
# -----------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------
# USER INPUT
# -----------------------

question = st.chat_input("Ask something about your documents...")

if question:

    st.chat_message("user").markdown(question)

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    if vectordb is None:

        response = "⚠️ Please upload and index documents first."

        st.chat_message("assistant").markdown(response)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

    else:

        retriever = vectordb.as_retriever(search_kwargs={"k": 4})

        docs = retriever.invoke(question)

        context = "\n\n".join([d.page_content for d in docs])

        prompt = f"""
        Use the context below to answer the question.
        Context:{context}
        Question:{question}"""

        with st.chat_message("assistant"):

            response_placeholder = st.empty()
            full_response = ""

            # streaming typing effect
            for chunk in llm.stream(prompt):

                full_response += chunk.content
                response_placeholder.markdown(full_response)

            # show sources
            sources = list(set([
                d.metadata.get("source", "Unknown")
                for d in docs
            ]))

            st.markdown("**Sources:**")

            for s in sources:
                st.markdown(f"- {s}")

        st.session_state.messages.append({
            "role": "assistant",
            "content": full_response
        })