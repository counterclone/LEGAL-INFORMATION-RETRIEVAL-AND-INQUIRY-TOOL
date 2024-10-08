import openai

system_content = "You are a travel agent. Be descriptive and helpful."
user_content = "Tell me about San Francisco"

client = openai.OpenAI(
    api_key="3952139433174d408c09c2d584a00dcb",
    base_url="https://api.aimlapi.com",
)

chat_completion = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    messages=[
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
    ],
    temperature=0.7,
    max_tokens=128,
)

response = chat_completion.choices[0].message.content
print("AI/ML API:\n", response)