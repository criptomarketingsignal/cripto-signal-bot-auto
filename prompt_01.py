# Código completo de prompt_01.py con integración de precio real y rango dinámico
codigo_prompt_01 = """
import os
import requests
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_CHAT_ID_ES = "-1002440626725"

def obtener_precio_btc():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "bitcoin",
            "vs_currencies": "usd"
        }
        response = requests.get(url, params=params)
        data = response.json()
        precio = data["bitcoin"]["usd"]
        return precio
    except Exception as e:
        print("Error al obtener el precio:", e)
        return None

def calcular_rango(precio):
    rango_min = round(precio * 0.985, 2)  # -1.5%
    rango_max = round(precio * 1.002, 2)  # +0.2%
    promedio = round((rango_min + rango_max) / 2, 2)
    return rango_min, rango_max, promedio

def send_prompt_01():
    fecha_hoy = datetime.now().strftime("%d de %B de %Y")
    precio_btc = obtener_precio_btc()

    if not precio_btc:
        return

    rango_min, rango_max, promedio = calcular_rango(precio_btc)

    prompt = (
        f"Actúa como un analista técnico profesional de criptomonedas. Hoy es {fecha_hoy}. "
        f"Basándote en el precio actual de Bitcoin ($ {precio_btc}), genera un análisis técnico y fundamental detallado "
        f"que indique un rango operable para el día en long (apalancamiento 3x), sin usar TP ni SL. "
        f"El rango sugerido debe estar entre ${rango_min} y ${rango_max}, con un promedio de entrada de ${promedio}. "
        f"Justifica ese rango con indicadores como velas, EMAs, RSI, Fibonacci, POC, SQZMOM y sentimiento del mercado. "
        f"Escríbelo con estructura profesional, usando ◉ y negritas en unicode como 𝐄𝐬𝐭𝐞 𝐞𝐣𝐞𝐦𝐩𝐥𝐨. Incluye una nota motivadora final "
        f"y especifica que es la señal 1 de 3 del día. El estilo debe ser ideal para Telegram, con emoticonos y claridad visual."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    message = response.choices[0].message["content"]

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
"""

# Guardar el archivo
file_path = "/mnt/data/prompt_01_precio_real.py"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(codigo_prompt_01.strip())

file_path
