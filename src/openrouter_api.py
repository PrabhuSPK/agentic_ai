import requests
import json
from openai import OpenAI
import time
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL") or "https://openrouter.ai/api/v1"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY", "")
MODEL = os.getenv("MODEL") or "openrouter/auto"

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

    try:
        models = client.models.list()
        available = {m.id for m in models.data}
        if MODEL not in available:
            free_models = [m.id for m in models.data if ":free" in m.id]
            print("Configured model not available:", MODEL)
            if free_models:
                print("Available free models:", ", ".join(free_models[:10]))
            MODEL = "openrouter/auto"
            print("Falling back to:", MODEL)
    except Exception:
        pass

    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "http://localhost:8000",  # Optional. Site URL for rankings
            "X-Title": "Local Testing",  # Optional. Site title for rankings
        },
        model=MODEL,
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
