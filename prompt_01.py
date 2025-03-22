import os
import requests
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_CHAT_ID_ES = "-1002440626725"

def send_prompt_01():
    fecha_hoy = datetime.now().strftime("%d de %B de %Y")

    prompt = (
        f"Actúa como un analista técnico profesional de criptomonedas. "
        f"Genera una señal para Bitcoin (BTC) en long con apalancamiento 3x para hoy, {fecha_hoy}. "
        "Incluye zona de entrada, promedio, TP, SL, análisis técnico (velas, RSI, EMAs, Fibonacci, volumen POC, SQZMOM), "
        "análisis fundamental (DXY, SP500, sentimiento). Escribe con estilo claro, estructurado, usando emoticonos, viñetas ◉ y negritas en unicode. "
        "Debe terminar con una nota motivadora y un botón de acceso a señales premium."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    mensaje = response.choices[0].message["content"]

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_CHAT_ID_ES,
        "text": mensaje,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "✨ Señales Premium 30 días GRATIS",
                        "url": "https://t.me/CriptoSignalBotGestion_bot?start=676731307b8344cb070ac996"
                    }
                ]
            ]
        }
    }

    requests.post(url, json=payload)
