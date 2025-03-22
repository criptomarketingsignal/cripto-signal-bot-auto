from datetime import datetime
import requests
import openai
import os

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

def send_prompt_01():
    fecha = obtener_fecha_en_espanol()

    prompt_es = f"""
Actúa como un analista técnico profesional de criptomonedas. Usa el modelo más reciente GPT-4o para generar un mensaje para Telegram, en español, dirigido a traders.

➡️ El mensaje debe contener datos reales y actuales del mercado, con un rango operable de al menos 2% entre entrada baja y alta. NO uses valores genéricos como "te daremos el rango más favorable". Usa precios reales actuales con análisis detallado.

➡️ El resultado debe estar redactado exactamente como este formato:

Buenos días traders! Que mejor manera de comenzar el día que con nuestra primera señal del día. Hoy vamos a analizar Bitcoin y darles nuestras recomendaciones. ¡Vamos allá!

𝐅𝐞𝐜𝐡𝐚: {fecha}
𝐒𝐞𝐧̃𝐚𝐥: 1 de 3

Nuestro equipo trabaja arduamente para ofrecer análisis técnico y fundamental en tiempo real tres veces al día, asegurándonos de mantener a nuestra comunidad completamente informada y preparada.

En nuestro análisis técnico, utilizamos las herramientas más confiables, como:
- Velas japonesas 📊
- Medias Móviles Exp 📈
- Fibonacci 🔢
- Fuerza Relativa (RSI) ⚖️
- SQZMOM ⚡️
- Volumen (POC) 💼

◉ 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐓𝐞́𝐜𝐧𝐢𝐜𝐨:
📊 Velas: [describe el patrón actual]
📈 EMAs: [comenta si hay cruce, soporte o tendencia]
🔁 Fibonacci: [menciona nivel de rebote o ruptura]
🧱 POC: [indica si hay acumulación/distribución]
⚡️ RSI: [nivel exacto + interpretación]
🚀 SQZMOM: [positivo o negativo, compresión o expansión]

◉ 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥:
💵 DXY: [comenta su tendencia]
🧠 Sentimiento: [positivo o negativo]
📈 Nasdaq/SP500: [relevancia en correlación con BTC]

◉ 𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧 (𝐋𝐨𝐧𝐠 𝟑𝐱):
💰 Entrada óptima entre: $[precio1] y $[precio2]
🎯𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧: Entre $[precio1] y $[precio2]
🟢 Porcentaje de efectividad estimado: [XX%]
Condiciones ideales para una operación intradía de alta probabilidad.
⚠️ ¡Cuida tu gestión de riesgo! Este mercado es altamente volátil. Operación válida solo para hoy.

📊 Señales, gráficos en vivo y análisis en tiempo real completamente GRATIS por 30 días.
🔑 𝐎𝐛𝐭𝐞́𝐧 𝐭𝐮 𝐦𝐞𝐬 𝐠𝐫𝐚𝐭𝐢𝐬 𝐚𝐡𝐨𝐫𝐚! 🚀

Gracias por elegirnos como tu portal de trading de confianza. ¡Juntos, haremos que tu inversión crezca!
✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨Mantente pendiente del mensaje de mitad de sesión. ¡Feliz trading!
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt_es}]
    )

    mensaje_es = response.choices[0].message["content"]

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload_es = {
        "chat_id": CHANNEL_CHAT_ID_ES,
        "text": mensaje_es,
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

    # Si deseas activarlo también para el canal en inglés, lo agregamos luego con su propio prompt_en.
