python --version  # Should be 3.9 or later
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows

pip install openai langchain


pip install -U langgraph "langchain[openai]"

delete .venv 

/Library/Frameworks/Python.framework/Versions/3.12/bin/python3 -m venv .venv