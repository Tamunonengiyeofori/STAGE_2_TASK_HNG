from dotenv import load_dotenv
import os
import openai

load_dotenv()

API_KEY = os.getenv("OPEN_API_SECRET_KEY")
openai.api_key = API_KEY

prompt = "write a tagline for an ice cream shop"

response = openai.Completion.create(
    engine="text-davinci-001", prompt=prompt, max_tokens=6, temperature=1)

print(response)