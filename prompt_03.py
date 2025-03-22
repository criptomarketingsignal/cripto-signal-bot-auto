import os
import requests
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_CHAT_ID_ES = "-1002440626725"
CHANNEL_CHAT_ID_EN = "-1002288256984"

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
    rango_min = round(precio * 0.99, 2)   # -1%
    rango_max = round(precio * 1.01, 2)   # +1%
    promedio = round((rango_min + rango_max) / 2, 2)
    efectividad = round(99.3 - abs(rango_max - rango_min) / precio * 100, 2)
    return rango_min, rango_max, promedio, efectividad

def obtener_fecha_es():
    meses = {
        "January": "enero", "February": "febrero", "March": "marzo",
        "April": "abril", "May": "mayo", "June": "junio",
        "July": "julio", "August": "agosto", "September": "septiembre",
        "October": "octubre", "November": "noviembre", "December": "diciembre"
    }
    hoy = datetime.now()
    mes = meses[hoy.strftime("%B")]
    return f"{hoy.day} de {mes} de {hoy.year}"

def send_prompt_01():
    precio_btc = obtener_precio_btc()
    if not precio_btc:
        return

    fecha_es = obtener_fecha_es()
    rango_min, rango_max, promedio, efectividad = calcular_rango_y_efectividad(precio_btc)

    # --- Español ---
    prompt_es = f"""
Actúa como un analista técnico profesional especializado en criptomonedas y genera un mensaje en español perfectamente estructurado para el canal de señales.

➡️ Crea un mensaje con estilo motivador, análisis real y visualmente claro para Telegram. El precio actual de BTC es {precio_btc} USD.

Usa esta estructura exacta en el mensaje generado:

Buenos días traders! Qué mejor manera de cerrar el día que con nuestra última señal. Analicemos cómo cerró Bitcoin y lo que se espera para mañana. ¡Vamos allá!

𝐅𝐞𝐜𝐡𝐚: {fecha_es}  
𝐒𝐞𝐧̃𝐚𝐥: 3 de 3

Nuestro equipo trabaja arduamente para ofrecer análisis técnico y fundamental en tiempo real tres veces al día, asegurándonos de mantener a nuestra comunidad completamente informada y preparada.

En nuestro análisis técnico, utilizamos las herramientas más confiables, como:
- Velas japonesas 📊
- Medias Móviles Exp 📈
- Fibonacci 🔢
- Fuerza Relativa (RSI) ⚖️
- (SQZMOM) ⚡️
- Volumen (POC) 💼

◉ 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐓𝐞́𝐜𝐧𝐢𝐜𝐨:
Incluye un análisis técnico claro basado en las herramientas anteriores.

◉ 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥:
Incluye visión del DXY, sentimiento de mercado, Nasdaq/SP500.

◉ 𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧 (𝐋𝐨𝐧𝐠 𝟑𝐱):
💰 Entrada óptima entre: ${rango_min} y ${rango_max}  
🎯𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧: Entre ${rango_min} – ${rango_max}  
🟢 Porcentaje de efectividad estimado: {efectividad}%  
Condiciones ideales para una operación intradía de alta probabilidad.  
⚠️ ¡Cuida tu gestión de riesgo! No te olvides de establecer una estrategia de salida. Este mercado es altamente volátil. Operación recomendada solo para hoy.

📊 Señales, gráficos en vivo y análisis en tiempo real completamente GRATIS por 30 días.  
🔑 𝐎𝐛𝐭𝐞́𝐧 𝐭𝐮 𝐦𝐞𝐬 𝐠𝐫𝐚𝐭𝐢𝐬 𝐚𝐡𝐨𝐫𝐚! 🚀  

Gracias por elegirnos como tu portal de trading de confianza. ¡Juntos, haremos que tu inversión crezca!  
✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨ Te esperamos mañana para nuevas oportunidades. ¡Feliz trading!
"""

    # --- English ---
    prompt_en = f"""
Act as a professional crypto technical analyst and generate a fully structured message for the signal channel in English.

➡️ Style: motivational tone, real analysis, and visually structured for Telegram. BTC current price is {precio_btc} USD.

Use this exact format:

Good evening traders! It's time for our final Bitcoin update of the day. Let’s review the close and prepare for tomorrow. Let's go!

📅 Date: {fecha_es}  
📌 Signal: 3 of 3

We work hard to deliver accurate technical and fundamental analysis in real time, three times a day, to keep our community informed and ready.

Tools we use:
- Candlesticks 📊
- EMAs 📈
- Fibonacci 🔢
- RSI ⚖️
- SQZMOM ⚡️
- POC Volume 💼

◉ 𝐓𝐞𝐜𝐡𝐧𝐢𝐜𝐚𝐥 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬:
Provide clear analysis based on those tools.

◉ 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬:
Include view of DXY, market sentiment, Nasdaq/SP500.

◉ 𝐎𝐩𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐑𝐚𝐧𝐠𝐞 (𝐋𝐨𝐧𝐠 𝟑𝐱):
💰 Ideal entry between: ${rango_min} and ${rango_max}  
🎯Operating range: From ${rango_min} – ${rango_max}  
🟢 Estimated success rate: {efectividad}%  
Perfect conditions for a high-probability intraday move.  
⚠️ Always manage your risk carefully. This is a high-volatility market. For today only.

📊 Get full access to real-time signals, charts and analysis for FREE during 30 days.  
🔑 𝐆𝐞𝐭 𝐲𝐨𝐮𝐫 𝐟𝐫𝐞𝐞 𝐦𝐨𝐧𝐭𝐡 𝐧𝐨𝐰! 🚀  

Thanks for choosing us as your trusted trading partner. Let’s grow your investments together.  
✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨ Be ready for tomorrow’s first update. Happy trading!
"""

    # --- Send to Spanish channel ---
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload_es = {
        "chat_id": CHANNEL_CHAT_ID_ES,
        "text": prompt_es,
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
    requests.post(url, json=payload_es)

    # --- Send to English channel ---
    payload_en = {
        "chat_id": CHANNEL_CHAT_ID_EN,
        "text": prompt_en,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "Free 30-day premium signals ✨",
                        "url": "https://t.me/CriptoSignalBotGestion_bot?start=676731307b8344cb070ac996"
                    }
                ]
            ]
        }
    }
    requests.post(url, json=payload_en)
