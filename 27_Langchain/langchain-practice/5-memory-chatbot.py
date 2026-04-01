from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

# 1. Setup the Model
llm = ChatOllama(model="gemma:2b")

# 2. Upgrade the Prompt
# Notice the new MessagesPlaceholder! This is where the memory gets injected.
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    MessagesPlaceholder(variable_name="chat_history"), 
    ("human", "{user_input}")
])

# Connect the basic chain
chain = prompt | llm 

# ==========================================
# 3. SET UP THE MEMORY STORAGE
# ==========================================
# We create a dictionary to hold our chat logs. 
# This allows us to have multiple different conversations (sessions) at once!
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        # If this is a new session, create a fresh notepad
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 4. Wrap the chain in the Memory Manager
# We tell it which chain to run, where to save the memory, and what our variables are named.
chatbot = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="user_input",
    history_messages_key="chat_history",
)

print("🧠 Memory-Aware Chatbot initialized! Type 'exit' to quit.\n")

# ==========================================
# 5. THE NEW CHAT LOOP
# ==========================================
while True:
    user_text = input("You: ")
    
    if user_text.lower() == 'exit':
        print("Goodbye!")
        break
        
    # We now invoke the 'chatbot' wrapper, NOT the raw chain.
    # We MUST pass a config dictionary to tell it which notepad (session) to use!
    response = chatbot.invoke(
        {"user_input": user_text},
        config={"configurable": {"session_id": "session_1"}}
    )
    
    print(f"AI: {response.content}\n")