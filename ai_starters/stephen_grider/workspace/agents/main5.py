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
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
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
    tools = refTools
)


# agentExecutor("How many users are in the database?")
# agentExecutor("How many users have provided a shipping address?")
agentExecutor("Summarize the top 5 most popular products. Write the results to a report file.")
