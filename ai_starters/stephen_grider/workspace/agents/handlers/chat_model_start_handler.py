from langchain.callbacks.base import BaseCallbackHandler

class ChatModelStartHandler(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, *, run_id, parent_run_id = None, tags = None, metadata = None, **kwargs):
        print(messages)
