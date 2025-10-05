from langchain.prompts import(
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from common.dev_config import chatllm

from langchain.agents import OpenAIFunctionsAgent,AgentExecutor

from agents.tools.sql import run_query_tool,list_tables

from langchain.schema import SystemMessage

tables = list_tables()
# print(tables)

prompt = ChatPromptTemplate(
    messages = [
        SystemMessage(content=f"You are an AI that has access to a SQLite database.\n{tables}"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)
refTools = [run_query_tool]

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


agentExecutor("How many users are in the database?")
