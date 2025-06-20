import os, openai, dotenv
dotenv.load_dotenv()

print("Loaded key preview:", os.getenv("OPENAI_API_KEY")[:8], "…")
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {"role": "user", "content": "Give me 3 bullet facts about post-TBI aggression."}
]

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0.3
)

print(response.choices[0].message.content)
