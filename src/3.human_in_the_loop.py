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

agent2 = ConversableAgent(
    "sara",
    llm_config=llm_config,
    system_message=(
        "You are playing a game of guess-my-number. You have the number 75 in your mind, "
        "and I will try to guess it.\n"
        "If my guess is much higher than your number, say 'too high'.\n"
        "If my guess is much lower than your number, say 'too low'.\n"
        "If my guess is only slightly higher (within 5), say 'high'.\n"
        "If my guess is only slightly lower (within 5), say 'low'.\n"
        "If I guess correctly, say 'correct'."
    ),
    human_input_mode="NEVER",
    is_termination_msg= lambda response:"75" in response["content"]
    )

## Human in the loop: ALWAYS
human_proxy = ConversableAgent(
    "human_proxy",
    llm_config=False,  # no LLM used for human proxy
    human_input_mode="ALWAYS",  # always ask for human input
)

human_proxy.initiate_chat(
    agent2,
    message="5",
   
)


