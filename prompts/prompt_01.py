import os
import requests
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_CHAT_ID_ES = "-1002440626725"
CHANNEL_CHAT_ID_EN = "-1002288256984"

def send_prompt_01():
    # Prompt en español
    prompt_es = (
        "Actúa como un analista técnico profesional de criptomonedas y genera una señal clara y precisa para Bitcoin "
        "con rango de entrada escalonado, niveles técnicos y justificación macro en español. Usa el estilo visual del Prompt 01."
    )

    # Prompt en inglés
    prompt_en = (
        "Act as a professional cryptocurrency technical analyst and generate a clear and precise signal for Bitcoin "
        "with a scalable entry range, technical levels, and macro justification in English. Use the visual style of Prompt 01."
    )

    # Generar mensaje en español
    response_es = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt_es}]
    )
    message_es = response_es.choices[0].message["content"]

    # Generar mensaje en inglés
    response_en = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt_en}]
    )
    message_en = response_en.choices[0].message["content"]

    # Enviar a canal en español
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload_es = {"chat_id": CHANNEL_CHAT_ID_ES, "text": message_es, "parse_mode": "HTML"}
    requests.post(url, data=payload_es)

    # Enviar a canal en inglés
    payload_en = {"chat_id": CHANNEL_CHAT_ID_EN, "text": message_en, "parse_mode": "HTML"}
    requests.post(url, data=payload_en)