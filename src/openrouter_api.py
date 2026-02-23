import os
import time
from autogen.agentchat import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    print("Missing API key. Set OPENROUTER_API_KEY or OPENAI_API_KEY (or use .env).")
    raise SystemExit(1)

user_prompt = input("Enter your prompt: ")

print("Sending request to OpenRouter via AutoGen...")
start_time = time.time()

config_list = [
    {
        "model": "deepseek/deepseek-r1-0528:free",
        "api_key": api_key,
        "base_url": "https://openrouter.ai/api/v1",
    }
]
llm_config = {"config_list": config_list, "timeout": 30}

assistant = AssistantAgent(name="assistant", llm_config=llm_config, system_message="You are a helpful assistant.")
user = UserProxyAgent(name="user", code_execution_config=False, human_input_mode="NEVER")

try:
    user.initiate_chat(assistant, message=user_prompt)
    end_time = time.time()
    print(f"Request completed in {end_time - start_time:.2f} seconds")
except Exception as e:
    end_time = time.time()
    print(f"Request failed after {end_time - start_time:.2f} seconds")
    print(f"Error: {e}")
