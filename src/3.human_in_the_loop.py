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
    system_message=(
        "I have a number in my mind, and you will try to guess it. "
        "If I say 'too high', you should guess a much lower number. "
        "If I say 'high', you should guess a slightly lower number. "
        "If I say 'too low', you should guess a much higher number. "
        "If I say 'low', you should guess a slightly higher number. "
        "Keep adjusting your guess based on the feedback until you get it right."
    ),
    human_input_mode="NEVER"
    )

agent2 = ConversableAgent(
    "sara",
    llm_config=llm_config,
    system_message=(
        "You are playing a game of guess-my-number. You have the number 65 in your mind, "
        "and I will try to guess it.\n"
        "If my guess is much higher than your number, say 'too high'.\n"
        "If my guess is much lower than your number, say 'too low'.\n"
        "If my guess is only slightly higher (within 5), say 'high'.\n"
        "If my guess is only slightly lower (within 5), say 'low'.\n"
        "If I guess correctly, say 'correct'."
    ),
    human_input_mode="NEVER",
    # max_consecutive_auto_reply=2
    is_termination_msg= lambda response:"65" in response["content"]
    )

agent2.initiate_chat(
    agent1,
    message="I have a number between 1 and 100. Guess it!",
    # max_turns=2
)

#initiate chat params - max_turns=1

#agentwise 
#1. max_consecutive_auto_reply=1
#2. is_termination_msg

