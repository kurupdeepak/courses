# dev_config.py

import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV", "dev").lower()
CHAT = os.getenv("CHAT", "false").lower()
chatllm = None

if ENV == "prod":
    print("🚀 Using OpenAI (prod)")
    modelToUse = "gpt-4o-mini"
    if CHAT == "true":
        from langchain_openai import ChatOpenAI
        chatllm = ChatOpenAI(model=modelToUse)
    else:
        from langchain_openai import OpenAI
        llm = OpenAI(model=modelToUse)  # or mistral, llama2, deepseek-coder
else:
    print("🛠️ Using Ollama (dev)")
    # from langchain_community.llms import Ollama
    modelToUse = "codellama"
    if CHAT == "true":
        from langchain_community.chat_models import ChatOllama
        chatllm = ChatOllama(model=modelToUse)
    else:
        from langchain_community.llms.ollama import OllamaRunnable
        llm = OllamaRunnable(model=modelToUse)  # or mistral, llama2, deepseek-coder

