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
    fecha_hoy = obtener_fecha_en_espanol()
    precio_btc = obtener_precio_btc()
    if not precio_btc:
        return

    rango_min, rango_max, efectividad = calcular_rango_y_efectividad(precio_btc)

    prompt_es = f"""
Actúa como un analista técnico profesional especializado en criptomonedas y genera un mensaje en español perfectamente estructurado para el canal de señales.

➡️ Crea un mensaje con estilo motivador, análisis real y visualmente claro para Telegram. El precio actual de BTC es {precio_btc} USD.

Usa esta estructura exacta en el mensaje generado:

¡Buenas noches traders! Qué mejor manera de cerrar el día que con nuestra última señal. Analicemos cómo cerró Bitcoin y lo que se espera para mañana. ¡Vamos allá!

𝐅𝐞𝐜𝐡𝐚: {fecha_hoy}  
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
💰 Entrada óptima entre: ${rango_min}
🎯𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧: Entre ${rango_min} – ${rango_max}  
🟢 Porcentaje de efectividad estimado: {efectividad}%  
Condiciones ideales para una operación intradía de alta probabilidad.  
⚠️ ¡Cuida tu gestión de riesgo! No te olvides de establecer una estrategia de salida. Este mercado es altamente volátil. Operación recomendada solo para hoy.

📊 Señales, gráficos en vivo y análisis en tiempo real completamente GRATIS por 30 días.  
🔑 𝐎𝐛𝐭𝐞́𝐧 𝐭𝐮 𝐦𝐞𝐬 𝐠𝐫𝐚𝐭𝐢𝐬 𝐚𝐡𝐨𝐫𝐚! 🚀  

Gracias por elegirnos como tu portal de trading de confianza. ¡Juntos, haremos que tu inversión crezca!  
✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨ Te esperamos mañana para nuevas oportunidades. ¡Feliz trading!
"""

    prompt_en = f"""
Translate this message into perfect English for a Telegram crypto trading channel audience, keeping the formatting, emojis, and tone:

{prompt_es}
"""

    response_es = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt_es}]
    )
    mensaje_es = response_es.choices[0].message["content"]

    response_en = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt_en}]
    )
    mensaje_en = response_en.choices[0].message["content"]

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    for canal, mensaje in [(CHANNEL_CHAT_ID_ES, mensaje_es), (CHANNEL_CHAT_ID_EN, mensaje_en)]:
        payload = {
            "chat_id": canal,
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

