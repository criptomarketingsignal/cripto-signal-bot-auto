import os
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

def obtener_fecha_en_ingles():
    return datetime.now().strftime("%B %d, %Y")

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
    rango_min = round(precio * 0.9925, 2)
    rango_max = round(precio * 1.0025, 2)
    promedio = round((rango_min + rango_max) / 2, 2)
    efectividad = round(99.35 - abs(rango_max - rango_min) / precio * 100, 2)
    return rango_min, rango_max, promedio, efectividad

def send_prompt_01():
    fecha_es = obtener_fecha_en_espanol()
    fecha_en = obtener_fecha_en_ingles()
    precio_btc = obtener_precio_btc()
    if not precio_btc:
        return

    rango_min, rango_max, promedio, efectividad = calcular_rango_y_efectividad(precio_btc)

    # Español
    prompt_es = f"""
Actúa como un analista técnico profesional especializado en criptomonedas y genera un mensaje en español perfectamente estructurado para el canal de señales.

Crea un mensaje con estilo motivador, análisis real y visualmente claro para Telegram. El precio actual de BTC es {precio_btc} USD.

Usa esta estructura exacta en el mensaje generado:

Buenos días traders! Qué mejor manera de comenzar el día que con nuestra primera señal del día. Hoy vamos a analizar Bitcoin y darles nuestras recomendaciones. ¡Vamos allá!

𝐅𝐞𝐜𝐡𝐚: {fecha_es}  
𝐒𝐞𝐧̃𝐚𝐥: 1 de 3

Nuestro equipo trabaja arduamente para ofrecer análisis técnico y fundamental en tiempo real tres veces al día, asegurándonos de mantener a nuestra comunidad completamente informada y preparada.

Herramientas utilizadas:
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
💰 Entrada óptima entre: ${rango_min}  
🎯𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧: Entre ${rango_min} – ${rango_max}  
🟢 Porcentaje de efectividad estimado: {efectividad}%  
Condiciones ideales para una operación intradía de alta probabilidad.  
⚠️ ¡Cuida tu gestión de riesgo! No te olvides de establecer una estrategia de salida. Este mercado es altamente volátil. Operación recomendada solo para hoy.

📊 Señales, gráficos en vivo y análisis en tiempo real completamente GRATIS por 30 días.  
🔑 𝐎𝐛𝐭𝐞́𝐧 𝐭𝐮 𝐦𝐞𝐬 𝐠𝐫𝐚𝐭𝐢𝐬 𝐚𝐡𝐨𝐫𝐚! 🚀  

Gracias por elegirnos como tu portal de trading de confianza. ¡Juntos, haremos que tu inversión crezca!  
✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨ Mantente pendiente del mensaje de mitad de sesión. ¡Feliz trading!
"""

    # Inglés
    prompt_en = f"""
Act as a professional crypto technical analyst and generate a perfectly structured message in English for the signals channel.

Write a motivational message, with real analysis and visually clean for Telegram. The current BTC price is {precio_btc} USD.

Use this exact structure:

Good morning traders! What better way to start the day than with our first signal. Today, we analyze Bitcoin and give you our top recommendations. Let’s go!

📅 Date: {fecha_en}  
📌 Signal: 1 of 3

Our team works hard to deliver real-time technical and fundamental analysis three times a day to keep you fully informed and ready.

Tools used:
- Japanese Candlesticks 📊
- Exponential Moving Averages 📈
- Fibonacci 🔢
- RSI ⚖️
- SQZMOM ⚡️
- Volume (POC) 💼

◉ 𝐓𝐞𝐜𝐡𝐧𝐢𝐜𝐚𝐥 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬:
Include real technical analysis using the above tools.

◉ 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬:
Include insights on DXY, market sentiment, Nasdaq/SP500.

◉ 𝐎𝐩𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐑𝐚𝐧𝐠𝐞 (𝐋𝐨𝐧𝐠 𝟑𝐱):
💰 Optimal entry between: ${rango_min}
🎯 Trading range: ${rango_min} – ${rango_max}  
🟢 Estimated success rate: {efectividad}%  
Ideal setup for an intraday high-probability move.  
⚠️ Always manage your risk. This market is volatile. Valid only for today.

📊 Real-time signals, live charts and full analysis FREE for 30 days.  
🔑 𝐂𝐥𝐚𝐢𝐦 𝐲𝐨𝐮𝐫 𝐅𝐑𝐄𝐄 𝐦𝐨𝐧𝐭𝐡 𝐧𝐨𝐰! 🚀  

Thanks for choosing us as your trusted trading hub. Together, we grow your investment!  
✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨ Stay tuned for the mid-session update. Happy trading!
"""

    response_es = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt_es}]
    )
    message_es = response_es.choices[0].message["content"]

    response_en = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt_en}]
    )
    message_en = response_en.choices[0].message["content"]

    url_photo = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    url_text = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    # Enviar imagen a ambos canales
    for chat_id in [CHANNEL_CHAT_ID_ES, CHANNEL_CHAT_ID_EN]:
        requests.post(url_photo, data={
            "chat_id": chat_id,
            "photo": "https://cryptosignalbot.com/wp-content/uploads/2025/03/21-1.png"
        })

    # Enviar texto a canal español
    payload_es = {
        "chat_id": CHANNEL_CHAT_ID_ES,
        "text": message_es,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [[{
                "text": "Señales premium 30 días gratis ✨",
                "url": "https://t.me/CriptoSignalBotGestion_bot?start=676731307b8344cb070ac996"
            }]]
        }
    }

    # Enviar texto a canal inglés
    payload_en = {
        "chat_id": CHANNEL_CHAT_ID_EN,
        "text": message_en,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [[{
                "text": "Free Premium Signals 30 Days ✨",
                "url": "https://t.me/CriptoSignalBotGestion_bot?start=676731307b8344cb070ac996"
            }]]
        }
    }

    requests.post(url_text, json=payload_es)
    requests.post(url_text, json=payload_en)
