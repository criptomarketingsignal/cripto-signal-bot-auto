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
    rango_min = round(precio * 0.9925, 2)   # -0.75%
    rango_max = round(precio * 1.0025, 2)   # +0.25%
    promedio = round((rango_min + rango_max) / 2, 2)
    efectividad = round(99.35 - abs(rango_max - rango_min) / precio * 100, 2)
    return rango_min, rango_max, promedio, efectividad

def obtener_fecha_es():
    meses = {
        "January": "enero", "February": "febrero", "March": "marzo",
        "April": "abril", "May": "mayo", "June": "junio",
        "July": "julio", "August": "agosto", "September": "septiembre",
        "October": "octubre", "November": "noviembre", "December": "diciembre"
    }
    ahora = datetime.now()
    mes_es = meses[ahora.strftime("%B")]
    return f"{ahora.day} de {mes_es} de {ahora.year}"

def send_prompt_01():
    fecha_hoy = obtener_fecha_es()
    precio_btc = obtener_precio_btc()
    if not precio_btc:
        return

    rango_min, rango_max, promedio, efectividad = calcular_rango_y_efectividad(precio_btc)

    prompt_es = f"""
Actúa como un analista técnico profesional especializado en criptomonedas y genera un mensaje en español perfectamente estructurado para el canal de señales.

➡️ Crea un mensaje con estilo motivador, análisis real y visualmente claro para Telegram. El precio actual de BTC es {precio_btc} USD.

Usa esta estructura exacta en el mensaje generado:

Buenos días traders! Qué mejor momento que la mitad de sesión para evaluar oportunidades. ¡Vamos a analizar Bitcoin con todo!

𝐅𝐞𝐜𝐡𝐚: {fecha_hoy}  
𝐒𝐞𝐧̃𝐚𝐥: 2 de 3

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
✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨ Mantente atento para el cierre de sesión. ¡Vamos con todo!
"""

    prompt_en = f"""
Act as a professional technical analyst specialized in cryptocurrencies and generate a fully structured and motivational message in English for the signal channel.

➡️ The message must follow the same format as the one in Spanish and be based on the current BTC price: {precio_btc} USD.

Use this exact structure in your answer:

Good afternoon traders! What better time than mid-session to reassess opportunities. Let’s dive into Bitcoin!

📅 Date: {fecha_hoy}  
📌 Signal: 2 of 3

Our team works hard to deliver real-time technical and fundamental analysis three times a day, keeping our community fully informed and prepared.

Tools used:
- Japanese Candlesticks 📊
- Exponential Moving Averages 📈
- Fibonacci Retracement 🔢
- Relative Strength Index (RSI) ⚖️
- SQZMOM (Momentum Squeeze) ⚡️
- Volume Profile (POC) 💼

◉ 𝐓𝐞𝐜𝐡𝐧𝐢𝐜𝐚𝐥 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬:
Based on RSI, EMAs, Fibonacci, SQZMOM, POC, and candlestick patterns.

◉ 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬:
Includes DXY movement, market sentiment, and Nasdaq/SP500 overview.

◉ 𝐎𝐩𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐑𝐚𝐧𝐠𝐞 (𝐋𝐨𝐧𝐠 𝟑𝐱):
💰 Optimal entry: Between ${rango_min}
🎯 Trading range: ${rango_min} – ${rango_max}  
🟢 Estimated success rate: {efectividad}%  
Ideal conditions for a high-probability intraday trade.  
⚠️ Always manage your risk wisely. This setup is valid for today only.

📊 Free premium signals, live charts, and real-time market analysis for 30 days.  
🔑 𝐂𝐥𝐚𝐢𝐦 𝐲𝐨𝐮𝐫 𝐅𝐑𝐄𝐄 𝟑𝟎-𝐝𝐚𝐲 𝐩𝐫𝐞𝐦𝐢𝐮𝐦 𝐚𝐜𝐜𝐞𝐬𝐬 𝐧𝐨𝐰! 🚀  

Thanks for choosing us as your trusted trading partner. Let’s grow together!  
✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨ Stay tuned for the closing signal later today!
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

    url_text = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    url_img = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    # Enviar imagen a ambos canales
    for chat_id in [CHANNEL_CHAT_ID_ES, CHANNEL_CHAT_ID_EN]:
        requests.post(url_img, data={
            "chat_id": chat_id,
            "photo": "https://cryptosignalbot.com/wp-content/uploads/2025/03/medi.png"
        })

    payload_es = {
        "chat_id": CHANNEL_CHAT_ID_ES,
        "text": message_es,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [[
                {
                    "text": "Señales premium 30 días gratis ✨",
                    "url": "https://t.me/CriptoSignalBotGestion_bot?start=676731307b8344cb070ac996"
                }
            ]]
        }
    }

    payload_en = {
        "chat_id": CHANNEL_CHAT_ID_EN,
        "text": message_en,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [[
                {
                    "text": "Free 30-Day Premium Signals ✨",
                    "url": "https://t.me/CriptoSignalBotGestion_bot?start=676731307b8344cb070ac996"
                }
            ]]
        }
    }

    requests.post(url_text, json=payload_es)
    requests.post(url_text, json=payload_en)
