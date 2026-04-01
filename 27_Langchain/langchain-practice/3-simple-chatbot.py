from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model = "gemma:2b"
)

parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful and concise AI assistant."),
    ("human", "{user_input}")
])

chain = prompt | llm | parser

while True:
    user_text = input("you: ")

    if user_text.lower() == 'exit':
        print("Goodbye!")
        break
    
    response = chain.invoke({"user_input" : user_text})

    print(f"AI: {response}\n")