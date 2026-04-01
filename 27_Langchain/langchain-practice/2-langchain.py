from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

# ====================== 1. Create the LLM ======================
llm = ChatOllama(
    model="gemma:2b",      # Change if you use different model
    temperature=0.3        # Controls creativity (0.0 = focused, 1.0 = creative)
)

# ====================== 2. Create Prompt Template ======================
prompt = ChatPromptTemplate.from_template(
    """You are a helpful assistant.

Question: {question}

Answer:"""
)

# ====================== 3. Create Output Parser ======================
parser = StrOutputParser()

# ====================== 4. Connect everything using LCEL ======================
chain = prompt | llm | parser

# ====================== 5. Run the chain ======================
question = "What is ChromaDB?"

response = chain.invoke({"question": question})

print("Question:", question)
print("\nAnswer:", response)