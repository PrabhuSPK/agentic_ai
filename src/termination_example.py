import os
from dotenv import load_dotenv
from autogen import AssistantAgent, ConversableAgent, UserProxyAgent

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

agent1 = ConversableAgent(
    "prabhu",
    llm_config=llm_config,
    system_message="You are duo standup comedian and you are good at telling jokes",
    human_input_mode="NEVER"
    )

agent2 = ConversableAgent(
    "sara",
    llm_config=llm_config,
    system_message="You are a duo standup comedian and you are good at telling jokes",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=2
    )

agent2.initiate_chat(
    agent1,
    message="Tell me a one line quote on marcus aurelius",
    # max_turns=2
)

#initiate chat params - max_turns=1
#agentwise 
#1. max_consecutive_auto_reply=1
#2. is_termination_msg

