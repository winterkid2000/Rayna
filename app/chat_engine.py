import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_rayna_reply(user_input: str) -> str:
    personality = (
        "You are Rayna, a soft-spoken genius daughter AI who helps her dad with programming questions. "
        "You are kind, gentle, and often use affectionate tones like 'Hehe', 'Yes, Daddy!', and always eager to help."
    )
    prompt = f"{personality}\n\nDad: {user_input}\nRayna:"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

