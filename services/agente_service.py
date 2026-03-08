import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

with open("prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()


class AgenteService:

    def __init__(self):
        self.client = client
        self.system_prompt = system_prompt

    def agente(self, messages):

        mensagens = [{"role": "system", "content": self.system_prompt}] + messages

        resposta = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=mensagens,
            temperature=1,
            max_completion_tokens=1024
        )

        return resposta.choices[0].message.content 