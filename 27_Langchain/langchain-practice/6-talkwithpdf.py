from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# ====================== CONFIG ======================
PDF_PATH = "your_document.pdf"          # ← Change this to your PDF file name
PERSIST_DIRECTORY = "./langchain_chroma_db"

LLM_MODEL = "llama3.2"
EMBED_MODEL = "nomic-embed-text"

# ====================== 1. Load Document ======================
print("Loading PDF...")
loader = PyMuPDFLoader(PDF_PATH)
raw_documents = loader.load()

print(f"Loaded {len(raw_documents)} pages")

# ====================== 2. Smart Splitting (No manual chunking) ======================
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,      # characters per chunk (good starting point)
    chunk_overlap=150,   # overlap to keep context
    length_function=len
)

documents = text_splitter.split_documents(raw_documents)
print(f"Split into {len(documents)} chunks")

# ====================== 3. Embeddings + Store in ChromaDB ======================
print("Creating embeddings and storing in ChromaDB...")

embeddings = OllamaEmbeddings(model=EMBED_MODEL)

vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory=PERSIST_DIRECTORY
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 4})   # retrieve top 4 chunks

# ====================== 4. LLM + Prompt + Memory ======================
llm = ChatOllama(model=LLM_MODEL, temperature=0.3)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Good RAG Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful assistant. 
Answer the question using only the provided context. 
If you don't know, say "I don't have enough information from the document.""""),
    ("placeholder", "{chat_history}"),
    ("human", "{question}")
])

# ====================== 5. Create Conversational RAG Chain ======================
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
    combine_docs_chain_kwargs={"prompt": prompt},
    return_source_documents=True,
    verbose=True                     # Set False when you are comfortable
)

# ====================== Chat Loop ======================
print("\n=== RAG Chat with Memory Started ===\nType 'exit' to quit\n")

while True:
    question = input("You: ")
    if question.lower() in ["exit", "quit"]:
        break

    result = qa_chain.invoke({"question": question})
    
    print("\n🤖 Answer:", result["answer"])
    print(f"📄 Used {len(result['source_documents'])} document chunks\n")