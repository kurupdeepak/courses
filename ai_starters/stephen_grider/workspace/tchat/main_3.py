from langchain.prompts import HumanMessagePromptTemplate,ChatPromptTemplate,MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from common.dev_config import chatllm
from langchain.chains import ConversationChain
from langchain_core.runnables import RunnablePassthrough
from langchain.memory import ConversationBufferMemory,FileChatMessageHistory,ConversationSummaryMemory
import sys
# Make CHAT=true 

if chatllm is None : 
    print("set the chat to true in the environment")
    sys.exit(1)

# convMemory = ConversationBufferMemory(
#     # chat_memory=FileChatMessageHistory("memory.json"),
#     memory_key="messages",
#     return_messages=True)
convMemory = ConversationSummaryMemory(
    # chat_memory=FileChatMessageHistory("memory.json"),
    llm = chatllm,
    memory_key="messages",
    return_messages=True)

chatPrompt = ChatPromptTemplate(
    input_variables=["content","messages"],
    messages = [
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)



# chain = chatPrompt | chatllm | memory
chain = LLMChain(
    llm=chatllm,
    prompt=chatPrompt,
    memory=convMemory,
    verbose=True
)


while True:
    content = input(">> ")

    print(f"You entered: {content}")

    # result = chain.invoke({"content":content})
    # result = chain.invoke({"input": content})
    result = chain({"content":content})
    # print(result["content"])
    print(result["text"])