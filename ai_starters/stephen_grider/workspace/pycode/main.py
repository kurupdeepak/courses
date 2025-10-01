from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI()

code_prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}",
    input_variables = ['language','task']
)

# code_chain = LLMChain(
#     llm=llm,
#     prompt=code_prompt
# )

# result = code_chain(
#     {
#         "language":"python",
#         "task":"return a list of numbers"
#     }
# )
# Run the chain
# result = code_chain.invoke({
#     "language": "python",
#     "task": "return a list of numbers"
# })

# Compose the chain
code_chain = code_prompt | llm

# Run it
result = code_chain.invoke({
    "language": "python",
    "task": "return a list of numbers"
    })
#add second chaing now next step


print(result)