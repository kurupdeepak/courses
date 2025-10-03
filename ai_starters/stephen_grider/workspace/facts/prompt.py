from common.dev_config import chatllm
from langchain.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
embeddings = OpenAIEmbeddings()


db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings
)
#
retriever = db.as_retriever()
#chain_type 
chain = RetrievalQA.from_chain_type(
    llm = chatllm,
    retriever=retriever,
    chain_type="stuff")

result = chain.run("What is an interesting fact about english language?")
