from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain,SequntialChain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI()

parser = StrOutputParser()

code_prompt = PromptTemplate.from_template(
    template="Write a very short {language} function that will {code}"
)

ut_gen_prompt = PromptTemplate.from_template(
    template="Write a test for the following {language} code:\n{code}"
)

# Compose the chain
code_chain = code_prompt | llm | parser | RunnableLambda(lambda output: {"language":"python","code": output})

# Step 2: Merge code with original language input
# merge_chain = RunnableLambda(lambda output, *, input: {
#     "language": input["language"],
#     **output  # adds "code": ...
# })

merge = RunnableLambda(
    lambda output,*,input : {
        # "language":input["language"],
        "language":"python",
        "code": output["code"]
    }
).with_config(run_input_keys=["language", "code"])

ut_gen_chain = ut_gen_prompt | llm | parser

# Run individual chain 
# result = code_chain.invoke({
#     "language": "python",
#     "code": "return a list of numbers"
#     })

# Run individual chain 

# result = ut_gen_chain.invoke({
#     "language": "python",
#     "code": "return a list of numbers"
#     })

composed_chain = code_chain | ut_gen_chain


result = composed_chain.invoke(
    {
        "language": "python",
        "code": "write a function to reverse a string"
    }
)


print(result)