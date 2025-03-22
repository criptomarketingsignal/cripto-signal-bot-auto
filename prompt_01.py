import os
import requests
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_CHAT_ID_ES = "-1002440626725"  # Canal en español

def send_prompt_01():
    fecha_hoy = datetime.now().strftime("%d de %B de %Y")

    prompt = (
        f"Actúa como un analista técnico profesional especializado en criptomonedas, y realiza un análisis completo, "
        f"detallado y claro del precio de Bitcoin para hoy, {fecha_hoy}. "
        "El análisis debe incluir multitemporalidades (1W, 1D, 4H, 1H), patrones de velas, niveles de soporte y resistencia, "
        "EMAs 21/55/100/200, retrocesos de Fibonacci (38.2%, 50%, 61.8%, 78.6%), volumen (POC), RSI, SQZMOM, análisis fundamental "
        "con eventos macroeconómicos relevantes, DXY, sentimiento del mercado, relación con SP500/Nasdaq, y determinar si es día para operar en long. "
        "Todo debe escribirse como una señal operativa clara con rango de entrada, TP, SL, efectividad estimada y mensaje motivador. "
        "Usa viñetas ◉ y negritas en unicode como 𝐞𝐬𝐭𝐞 𝐭𝐢𝐩𝐨. Termina con un llamado a la acción motivador. "
        "Es la primera señal del día, así que menciónalo al principio."
    )

    # Solicitar análisis a OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    message = response.choices[0].message["content"]

    # Enviar mensaje a Telegram con botón
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_CHAT_ID_ES,
        "text": message,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "Señales premium 30 días gratis ✨",
                        "url": "https://t.me/CriptoSignalBotGestion_bot?start=676731307b8344cb070ac996"
                    }
                ]
            ]
        }
    }

    requests.post(url, json=payload)
