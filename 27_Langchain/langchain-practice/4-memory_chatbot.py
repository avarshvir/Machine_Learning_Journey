from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# 1. Create LLM
llm = ChatOllama(
    model="gemma:2b",
    temperature=0.7
)

# 2. Create Memory
memory = ConversationBufferMemory(
    memory_key="history",      # This is important
    return_messages=True
)

# 3. Create Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly and helpful assistant. Keep the conversation natural."),
    ("placeholder", "{history}"),           # This will automatically put chat history
    ("human", "{input}")
])

# 4. Create the Chain with Memory
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=True                    # Set to True to see what is happening inside
)

# 5. Start Chatting
print("Memory-Aware Chatbot Started! (Type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    
    response = conversation.invoke({"input": user_input})
    print("Bot:", response["response"])
    print("-" * 50)