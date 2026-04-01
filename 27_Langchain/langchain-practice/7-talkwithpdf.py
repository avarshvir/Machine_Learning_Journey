from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

# 1. LOAD AND SPLIT (Automated)
loader = PyPDFLoader("document.pdf")
# Recursive splitting keeps paragraphs together whenever possible
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = loader.load_and_split(text_splitter)

# 2. CREATE VECTOR STORE (The Library)
# We use Ollama to create the embeddings (numbers) for our chunks
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma.from_documents(documents=docs, embedding=embeddings)
retriever = vectorstore.as_retriever()

# 3. SETUP THE BRAIN (The LLM)
llm = ChatOllama(model="llama3")

# 4. THE RAG PROMPT
# Notice we now have {context} for the PDF data and {chat_history} for memory
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer the user's question using ONLY this context: {context}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{user_input}")
])

# 5. THE CHAIN (The Assembly Line)
# This part gets slightly more complex because we need to 'retrieve' data first
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# This is a simplified logic flow:
# 1. Retrieve docs -> 2. Format them -> 3. Pass to Prompt -> 4. LLM
from langchain_core.runnables import RunnablePassthrough

rag_chain = (
    {"context": retriever | format_docs, "user_input": RunnablePassthrough()}
    | prompt
    | llm
)

# 6. ADD MEMORY WRAPPER
store = {}
def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

final_rag_bot = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="user_input",
    history_messages_key="chat_history",
)

# Run it!
print("📚 RAG Chatbot Ready.")