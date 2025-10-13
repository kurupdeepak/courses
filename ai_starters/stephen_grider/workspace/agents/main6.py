from langchain.prompts import(
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from common.dev_config import chatllm

from langchain.agents import OpenAIFunctionsAgent,AgentExecutor

from agents.tools.sql import run_query_tool,list_tables,describe_tables_tool

from agents.tools.report import write_report_tool

from langchain.schema import SystemMessage

from langchain.memory import ConversationBufferMemory

tables = list_tables()
# print(tables)

prompt = ChatPromptTemplate(
    messages = [
        SystemMessage(content=(
            f"You are an AI that has access to a SQLite database.\n"
            f"The database has tables of:{tables}"
            "Do not make any assumptions about what tables exist "
            "or what columns exist. Instead, use the 'describe_tables' function"
        )),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

chatHistory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

refTools = [run_query_tool,describe_tables_tool,write_report_tool]

agent = OpenAIFunctionsAgent(
    llm = chatllm,
    prompt=prompt,
    tools=refTools
)

agentExecutor = AgentExecutor(
    agent = agent,
    verbose=True,
    tools = refTools,
    memory=chatHistory
)


# agentExecutor("How many users are in the database?")
# agentExecutor("How many users have provided a shipping address?")
# agentExecutor("Summarize the top 5 most popular products. Write the results to a report file.")
agentExecutor(
    "How many orders are there? Write the result to an html report."
)

agentExecutor(
    "Repeat the exact same process for users"
)
