from dotenv import load_dotenv
import os
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv() 


print("🧪 Testing OPENAI_API_KEY from envFile...")

llm = OpenAI()


# Define prompt using LangChain's PromptTemplate
prompt = PromptTemplate.from_template("{question}")

result = llm.invoke("How are you?")

# Compose the chain
chain = prompt | llm

# Run it
result = chain.invoke({"question": "How are you?"})
print(result)