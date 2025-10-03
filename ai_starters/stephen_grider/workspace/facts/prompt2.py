from common.dev_config import chatllm
from langchain.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from custom_reduntant_filter_retriever import CustomRedundantFilterRetriever
import langchain

langchain.debug = True

embeddings = OpenAIEmbeddings()

db = Chroma(
    embedding=embeddings,
    persist_directory="emb"
)

retriever = CustomRedundantFilterRetriever(
    embeddings=embeddings,
    chroma = db
)

#chain_type 
chain = RetrievalQA.from_chain_type(
    llm = chatllm,
    retriever=retriever,
    chain_type="stuff")

result = chain.run("What is an interesting fact about english language?")
