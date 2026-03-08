import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key= os.getenv("GROQ_API_KEY"))

with open("prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()


def agente(messages):

    mensagens = [{"role": "system", "content": system_prompt}] + messages

    resposta = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=mensagens,
        temperature=1,
        max_completion_tokens=8192
    )

    return resposta.choices[0].message.content