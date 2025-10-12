import os
from dotenv import load_dotenv
from openai import OpenAI

# Load from .env
load_dotenv()

# Debugging check
print("API KEY (first 10 chars):", str(os.getenv("OPENAI_API_KEY"))[:10])

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello from Starfleet"}],
    max_tokens=10
)

print(resp.choices[0].message.content)


