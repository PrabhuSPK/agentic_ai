import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

# llm_config = { "config_list": [{ "model": "gpt-4", "api_key": os.environ.get("OPENAI_API_KEY") }] }

llm_config = {
    "config_list": [
        {
            "base_url": os.getenv("BASE_URL"),
            "api_key": os.getenv("OPENROUTER_API_KEY"),
            "model": "nvidia/nemotron-nano-12b-v2-vl:free",
        }
    ]
}

assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent("user_proxy", code_execution_config=False)

user_proxy.initiate_chat(
    assistant,
    message= "Tell me a joke on data scientists"
)