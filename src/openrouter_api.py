import requests
import json
from openai import OpenAI
import time

# Your OpenRouter API key
OPENROUTER_API_KEY = "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" #put openrouter api key here

# Get user input
user_prompt = input("Enter your prompt: ")

print("Sending request to OpenRouter API...")
start_time = time.time()

try:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
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
