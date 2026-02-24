import os
from dotenv import load_dotenv

load_dotenv()

baseurl = os.getenv("BASE_URL")
print(baseurl)  
print(os.getenv("OPENROUTER_API_KEY"))