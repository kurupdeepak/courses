from langchain.prompts import HumanMessagePromptTemplate,ChatPromptTemplate
from langchain_openai import ChatOpenAI
from common.dev_config import chatllm
import sys

if chatllm is None : 
    print("set the chat to true in the environment")
    sys.exit(1)

# Make CHAT=true 
prompt = ChatPromptTemplate.from_messages(
    messages=[
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = prompt | chatllm 

while True:
    content = input(">> ")

    print(f"You entered: {content}")

    result = chain.invoke({"content":content})

    print(result.content)