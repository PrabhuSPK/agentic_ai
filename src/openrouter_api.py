import requests
import json
from openai import OpenAI
import time
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
# Your OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Get user input
user_prompt = input("Enter your prompt: ")

print("Sending request to OpenRouter API...")
start_time = time.time()

try:
    client = OpenAI(
        base_url=BASE_URL,
        api_key=OPENROUTER_API_KEY,
        timeout=30.0  # 30 second timeout
    )

    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "http://localhost:8000",  # Optional. Site URL for rankings
            "X-Title": "Local Testing",  # Optional. Site title for rankings
        },
        model="deepseek/deepseek-r1-0528:free",
        messages=[
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        timeout=30.0  # 30 second timeout
    )
    
    end_time = time.time()
    print(f"Request completed in {end_time - start_time:.2f} seconds")
    
    print("\nAI Response:")
    print("-" * 50)
    print(completion.choices[0].message.content)
    print("-" * 50)
    
except Exception as e:
    end_time = time.time()
    print(f"Request failed after {end_time - start_time:.2f} seconds")
    print(f"Error: {e}")
    print("\nThis could be due to:")
    print("1. API key issues")
    print("2. Model availability")
    print("3. Network connectivity")
    print("4. Rate limiting")
