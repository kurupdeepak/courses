from dotenv import load_dotenv
import os
from langchain_openai import OpenAI

load_dotenv() 


print("🧪 Testing OPENAI_API_KEY from envFile...")
# print("OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))

llm = OpenAI()

result = llm.invoke("How are you?")

# print(result)
print(result.output_text)