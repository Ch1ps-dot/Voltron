from openai import OpenAI
from ..configs import settings

def login():
    try:
      client = OpenAI(
        base_url=settings.base_url,
        api_key=settings.api_key
      )
    except Exception as e:
        print("Connection Error")
    
    print("Loggin Success")
    return client

def chatllm(clt, msg: str = ""):
    try:
      completion = clt.chat.completions.create(
        model=settings.model,
        messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": msg}
        ]
      )
    except Exception as e:
       print("Chat Error")
    
    response: str = completion.choices[0].message['content']

    return response
  