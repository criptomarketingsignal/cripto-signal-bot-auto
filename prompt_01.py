# Integrar el prompt dentro del código de generación final en prompt_01.py
codigo_integrado = """
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

    prompt = f\"\"\"
Actúa como un analista técnico profesional especializado en criptomonedas y genera un análisis claro, estructurado y motivador para Bitcoin (BTCUSD) en español.

➡️ Hoy es {fecha_hoy}. Esta es la **Señal 1 de 3 del día**.
➡️ El análisis debe enfocarse en identificar un **rango operable para el día** (únicamente en long con apalancamiento 3x), basado en el precio actual de BTC, que es de aproximadamente ${precio_btc}.

◉ El rango debe estar entre ${rango_min} – ${rango_max}, con un promedio de entrada de ${promedio}.
◉ Justifica por qué operar en ese rango con análisis técnico y fundamental.
◉ No incluyas Take Profit ni Stop Loss, solo el rango ideal para abrir y cerrar operaciones escalonadas durante el día.

Estructura el mensaje con estos elementos:
- Introducción motivadora
- 𝐅𝐞𝐜𝐡𝐚 y "Señal 1 de 3"
- 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐓𝐞́𝐜𝐧𝐢𝐜𝐨 (Velas, EMAs, Fibonacci, RSI, SQZMOM, POC)
- 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥 (DXY, Nasdaq/SP500, sentimiento)
- 𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧 (𝐋𝐨𝐧𝐠 𝟑𝐱) con entrada recomendada y promedio
- Advertencia sobre gestión de riesgo

Finaliza con este bloque promocional:

📈 𝐓𝐫𝐚𝐝𝐢𝐧𝐠 𝐞𝐧 𝐓𝐢𝐞𝐦𝐩𝐨 𝐑𝐞𝐚𝐥 | 𝐏𝐫𝐞𝐜𝐢𝐬𝐢𝐨́𝐧 𝐌𝐚́𝐱𝐢𝐦𝐚 | 𝐑𝐞𝐬𝐮𝐥𝐭𝐚𝐝𝐨𝐬 𝐂𝐨𝐦𝐩𝐫𝐨𝐛𝐚𝐝𝐨𝐬

𝐒𝐞𝐧̃𝐚𝐥𝐞𝐬 𝐝𝐞 𝐓𝐫𝐚𝐝𝐢𝐧𝐠 𝐜𝐨𝐧 𝐄́𝐱𝐢𝐭𝐨 𝐆𝐚𝐫𝐚𝐧𝐭𝐢𝐳𝐚𝐝𝐨:
🔥 𝐅𝐈𝐑𝐄 𝐒𝐜𝐚𝐥𝐩𝐢𝐧𝐠 – 🏅 85.64% – 🟢 1,563 ganadoras – 🔴 262 perdedoras
💎 𝐄𝐋𝐈𝐓𝐄 𝐒𝐜𝐚𝐥𝐩𝐢𝐧𝐠 – 🏅 99.10% – 🟢 552 ganadoras – 🔴 5 perdedoras
🪙 𝐃𝐄𝐋𝐓𝐀 𝐒𝐰𝐢𝐧𝐠 – 🏅 96.00% – 🟢 48 ganadoras – 🔴 2 perdedoras

📊 Señales, gráficos en vivo y análisis en tiempo real completamente GRATIS por 30 días.  
🔑 𝐎𝐛𝐭𝐞́𝐧 𝐭𝐮 𝐦𝐞𝐬 𝐠𝐫𝐚𝐭𝐢𝐬 𝐚𝐡𝐨𝐫𝐚! 🚀
\"\"\"

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

