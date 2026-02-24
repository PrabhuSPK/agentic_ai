import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()

# llm_config = { "config_list": [{ "model": "gpt-4", "api_key": os.environ.get("OPENAI_API_KEY") }] }

llm_config = {
    "config_list": [
        {
            "base_url": os.getenv("BASE_URL"),
            "api_key": os.getenv("OPENROUTER_API_KEY"),
            "model": os.getenv("MODEL_NAME"),
        }
    ]
}

assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)
#user=>agent=>llm=>agent
user_proxy.initiate_chat(
    assistant,
    message= "Tell me a joke on data scientists" #user
)