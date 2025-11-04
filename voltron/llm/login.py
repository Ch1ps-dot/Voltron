from openai import OpenAI
from configs import settings

client = OpenAI(
    base_url=settings.base_url,
    api_key=settings.api_key
)
completion = client.chat.completions.create(
  model=settings.model,
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)
print(completion.choices[0].message)