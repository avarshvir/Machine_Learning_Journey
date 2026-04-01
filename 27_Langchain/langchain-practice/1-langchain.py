from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

print("Starting the LangChain assembly line...")

llm = ChatOllama(
    model="gemma:2b"    
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful teacher. Keep your answers to exactly one sentence."),
    ("human", "Explain {topic} to me.")
])

parser = StrOutputParser()

# pass the prompt to llm and pass the llm to parser
chain = prompt | llm | parser

print("Chain built! Sending data through...")

final_result = chain.invoke({"topic": "Machine Learning"})

print("\n--- AI OUTPUT ---")
print(final_result)