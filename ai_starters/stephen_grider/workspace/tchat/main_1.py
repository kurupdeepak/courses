from langchain.prompts import HumanMessagePromptTemplate,ChatPromptTemplate,MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from common.dev_config import chatllm
from langchain.chains import ConversationChain
from langchain_core.runnables import RunnablePassthrough
from langchain.memory import ConversationBufferMemory
import sys
# Make CHAT=true 

if chatllm is None : 
    print("set the chat to true in the environment")
    sys.exit(1)

chatPrompt = ChatPromptTemplate(
    input_variables=["content"],
    messages = [
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = chatPrompt | chatllm

while True:
    content = input(">> ")

    print(f"You entered: {content}")

    # result = chain.invoke({"content":content})
    result = chain.invoke({"content": content})

    print(result.content)
    # print(result)