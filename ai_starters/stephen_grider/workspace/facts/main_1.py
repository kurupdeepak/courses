# from common.dev_config import llm
from langchain.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

# will cost money
embeddings = OpenAIEmbeddings()


# emb = embeddings.embed_query("hi there")

# print(emb)

textSplitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0
)
loader = TextLoader("facts.txt")

# doc = loader.load()
docs = loader.load_and_split(text_splitter=textSplitter)

db = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="emb"
)
# for doc in docs:
#     print(doc.page_content)
#     print("\n")

# results = db.similarity_search_with_score("What is an interesting fact about english language?")
# k = result count most relevant
# results = db.similarity_search_with_score("What is an interesting fact about english language?",
results = db.similarity_search("What is an interesting fact about english language?",
                                          k=1)

# for result in results:
#     print("\n")
#     print(result[1])
#     print(result[0].page_content)

for result in results : 
    print("\n")
    print(result.page_content)