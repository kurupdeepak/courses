python --version  # Should be 3.9 or later
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows

pip install openai langchain


pip install -U langgraph "langchain[openai]"

delete .venv 

/Library/Frameworks/Python.framework/Versions/3.12/bin/python3 -m venv .venv

<!-- OLLAMA -->
brew install ollama   # macOS # downloading from ollama website application worked
#pull a model 
ollama run llama2
#for a coding model 
ollama run codellama

pip install langchain-community (Ollama is deprecated)

pip install -U langchain-community

check if the server is running 
curl http://localhost:11434
-----------------
Section 1 - ChatGPT and Langchain integration


brew install sqlite
--> sqlite3 <db-path>
SQLite Viewer extension