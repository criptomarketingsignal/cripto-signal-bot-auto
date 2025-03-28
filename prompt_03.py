import os
import json
import requests
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_CHAT_ID_ES = "-1002440626725"
CHANNEL_CHAT_ID_EN = "-1002288256984"

def obtener_fecha_en_espanol():
    meses = {
        "January": "enero", "February": "febrero", "March": "marzo",
        "April": "abril", "May": "mayo", "June": "junio",
        "July": "julio", "August": "agosto", "September": "septiembre",
        "October": "octubre", "November": "noviembre", "December": "diciembre"
    }
    hoy = datetime.now()
    mes = meses[hoy.strftime("%B")]
    return f"{hoy.day} de {mes} de {hoy.year}"

def obtener_precio_btc():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": "bitcoin", "vs_currencies": "usd"}
        response = requests.get(url, params=params)
        data = response.json()
        return float(data["bitcoin"]["usd"])
    except Exception as e:
        print("❌ Error al obtener precio BTC:", e)
        return None

def calcular_rango_y_efectividad(precio):
    rango_min = round(precio * 0.988, 2)
    rango_max = round(precio * 1.012, 2)
    efectividad = round(100 - abs(rango_max - rango_min) / precio * 100, 2)
    return rango_min, rango_max, efectividad

def send_prompt_01():
    fecha_es = obtener_fecha_en_espanol()
    today_date = datetime.now().strftime("%B %d, %Y")
    precio_btc = obtener_precio_btc()
    if not precio_btc:
        return

    rango_min, rango_max, efectividad = calcular_rango_y_efectividad(precio_btc)

    prompt_es = f"""
    Actúa como un analista técnico profesional especializado en criptomonedas. Tu objetivo es generar un análisis estructurado y preciso del comportamiento de Bitcoin (BTCUSD), enfocado únicamente en operaciones LONG de corto plazo. El análisis se basa en el gráfico de 1 hora, pero debe considerar múltiples temporalidades y factores macroeconómicos El precio actual de BTC es {precio_btc} USD..

    🧠 Utiliza indicadores técnicos como:
    - Velas japonesas
    - EMAs (21, 55, 100, 200)
    - RSI
    - SQZMOM
    - Volumen (POC)
    - Retrocesos de Fibonacci en 1D y 4H (solo para análisis interno, no mostrar en el mensaje)
    
    Además, evalúa eventos macroeconómicos o políticos importantes (FED, CPI, datos de empleo, declaraciones de Trump u otros líderes, conflictos globales, etc.) para reforzar o rechazar la validez de operar hoy.

⬅️ Crea un mensaje con estilo motivador, análisis real y visualmente claro para Telegram. El precio actual de BTC es {precio_btc} USD.

Usa esta estructura exacta en el mensaje generado:

¡Buenas noches traders! Qué mejor manera de cerrar el día que con nuestra última señal. Analicemos cómo cerró Bitcoin y lo que se espera para mañana. ¡Vamos allá!

𝗖𝗲𝗳𝘀: {fecha_es}  
𝗔𝗲𝘇𝗲𝗮: 3 de 3

Nuestro equipo trabaja arduamente para ofrecer análisis técnico y fundamental en tiempo real tres veces al día, asegurándonos de mantener a nuestra comunidad completamente informada y preparada.
"""

    prompt_en = f"""
Act as a professional technical analyst specialized in cryptocurrencies. Your goal is to generate a well-structured and accurate analysis of Bitcoin (BTCUSD), focused exclusively on short-term LONG operations. The analysis must be based on the 1-hour chart, but should also consider multiple timeframes and macroeconomic factors. The current BTC price is {precio_btc} USD.

🧠 Use technical indicators such as:
- Japanese candlesticks
- EMAs (21, 55, 100, 200)
- RSI
- SQZMOM
- Volume (POC)
- Fibonacci retracements on 1D and 4H (internal use only, do not show in final message)

Also, evaluate key macroeconomic or political events (FED meetings, CPI, employment data, statements from Trump or other global leaders, international conflicts, etc.) to validate or reject the decision to operate today.

Use this exact structure in the generated message:

Good evening traders! What better way to end the day than with our final signal. Let’s analyze how Bitcoin closed and what to expect for tomorrow. Let’s go!

𝐃𝐚𝐭𝐞: {today_date}  
𝐒𝐢𝐠𝐧𝐚𝐥: 3 of 3

Our team works hard to provide real-time technical and fundamental analysis three times a day, ensuring our community stays fully informed and prepared.
"""

    try:
        response_es = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt_es}]
        )
        message_es = response_es.choices[0].message["content"]

        response_en = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt_en}]
        )
        message_en = response_en.choices[0].message["content"]

        url_photo = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        url_text = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        # Enviar imagen a ambos canales
        for chat_id in [CHANNEL_CHAT_ID_ES, CHANNEL_CHAT_ID_EN]:
            requests.post(url_photo, data={
                "chat_id": chat_id,
                "photo": "https://cryptosignalbot.com/wp-content/uploads/2025/03/principio.png"
            })

        # Enviar texto a canal español
        payload_es = {
            "chat_id": CHANNEL_CHAT_ID_ES,
            "text": message_es,
            "parse_mode": "HTML",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{
                    "text": "🎯 Señales premium 30 días gratis",
                    "url": "https://t.me/CriptoSignalBotGestion_bot?start=676731307b8344cb070ac996"
                }]]
            })
        }

        # Enviar texto a canal inglés
        payload_en = {
            "chat_id": CHANNEL_CHAT_ID_EN,
            "text": message_en,
            "parse_mode": "HTML",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{
                    "text": "🎯 Free Premium Signals 30 Days",
                    "url": "https://t.me/CriptoSignalBotGestion_bot?start=676731307b8344cb070ac996"
                }]]
            })
        }

        requests.post(url_text, json=payload_es)
        requests.post(url_text, json=payload_en)
