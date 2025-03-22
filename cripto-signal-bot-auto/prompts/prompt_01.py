import os
import requests
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_prompt_01():
    prompt = (
        "Actúa como un analista técnico profesional de criptomonedas y genera una señal clara y precisa para Bitcoin "
        "con rango de entrada escalonado, niveles técnicos y justificación macro. Usa el estilo visual del Prompt 01."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    message = response.choices[0].message["content"]

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    requests.post(url, data=payload)