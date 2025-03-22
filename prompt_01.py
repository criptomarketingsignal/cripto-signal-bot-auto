import os
import requests
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_CHAT_ID_ES = "-1002440626725"

def send_prompt_01():
    fecha_hoy = datetime.now().strftime("%d de %B de %Y")

    # Prompt para el análisis intermedio con profundidad técnica
    prompt_analisis_es = (
        f"Actúa como un analista técnico profesional especializado en criptomonedas y genera la primera señal operativa del día "
        f"para Bitcoin (BTCUSD) con apalancamiento 3x. La fecha es {fecha_hoy}. "
        "El análisis debe incluir: velas japonesas (1W, 1D, 4H, 1H), soportes/resistencias, EMAs (21, 55, 100, 200), retrocesos de Fibonacci (4H y 1D), "
        "volumen (POC), RSI, SQZMOM y un análisis fundamental breve (FED, DXY, sentimiento de mercado, SP500/Nasdaq). "
        "Determina si hoy es buen día para operar en LONG. Indica precio de entrada y precio de salida si el patrón se rompe. "
        "No uses un rango fijo, calcula el rango de entrada dinámicamente. "
        "El estilo debe ser motivador, profesional y visualmente claro con ◉ y negritas unicode como 𝐄𝐬𝐭𝐨. "
        "Agrega un mensaje de cierre que diga: '𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 te acompaña en cada operación. ¡Nos vemos en la mitad de sesión!' "
    )

    # Llamada a la API de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt_analisis_es}]
    )
    mensaje = response.choices[0].message["content"]

    # Enviar a Telegram con botón único
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_CHAT_ID_ES,
        "text": mensaje,
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
