import os
from groq import Groq



def get_completion(prompt, model="openai/gpt-oss-120b"):
    client = Groq(api_key=os.environ['GROQ_API_KEY'])
    messages = [
        {
            "role": "user",
            "content": f"{prompt}"
        }
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content