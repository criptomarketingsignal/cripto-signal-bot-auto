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
    rango_min = round(precio * 0.9925, 2)
    rango_max = round(precio * 1.0025, 2)
    promedio = round((rango_min + rango_max) / 2, 2)
    efectividad = round(99.35 - abs(rango_max - rango_min) / precio * 100, 2)
    return rango_min, rango_max, promedio, efectividad

def send_prompt_01():
    fecha_es = obtener_fecha_en_espanol()
    precio_btc = obtener_precio_btc()
    if not precio_btc:
        return

    rango_min, rango_max, promedio, efectividad = calcular_rango_y_efectividad(precio_btc)

    prompt_resumen = f"""
Genera un mensaje en español corto (máximo 950 caracteres) para Telegram con estilo motivador y profesional sobre la apertura del día con Bitcoin. Usa solo estas viñetas ◉, esta tipografía 𝐨𝐬𝐜𝐮𝐫𝐚 para negrillas y emoticonos. El precio actual de BTC es {precio_btc} USD. Incluye fecha, título, breve análisis visual de la imagen y llamado a revisar el análisis completo. No des rangos ni porcentajes aquí.
"""

    prompt_extenso = f"""
Actúa como un analista técnico profesional especializado en criptomonedas y genera un análisis completo y detallado para Bitcoin (BTCUSD) hoy, {fecha_es}. Usa el siguiente formato con subtítulos claros:

𝐏𝐀𝐒𝐎 𝟏: ¿𝐏𝐚𝐫𝐚 𝐪𝐮𝐞́ 𝐟𝐞𝐜𝐡𝐚 𝐝𝐞𝐬𝐞𝐚𝐬 𝐞𝐥 𝐚𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐝𝐞 𝐁𝐢𝐭𝐜𝐨𝐢𝐧?
Hoy, {fecha_es}

𝐏𝐀𝐒𝐎 𝟐: 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐓𝐞́𝐜𝐧𝐢𝐜𝐨 𝐌𝐮𝐥𝐭𝐢𝐭𝐞𝐦𝐩𝐨𝐫𝐚𝐥
◉ Velas japonesas (1W, 1D, 4H, 1H) con patrones y estructuras clave.
◉ Soportes y resistencias por temporalidad y con EMAs 21, 55, 100, 200.
◉ Retrocesos de Fibonacci en 4H y 1D (38.2%, 50%, 61.8%, 78.6%).
◉ Volumen POC: zonas de acumulación/distribución.
◉ RSI: valores en 1H, 4H y 1D con divergencias si aplica.
◉ SQZMOM: compresión/expansión y dirección del momentum.

𝐏𝐀𝐒𝐎 𝟑: 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥
◉ Eventos macroeconómicos importantes.
◉ Movimiento del índice DXY.
◉ Sentimiento del mercado y redes sociales.
◉ Correlación con SP500/Nasdaq.

𝐏𝐀𝐒𝐎 𝟒: 𝐒𝐢𝐧𝐭𝐞𝐬𝐢𝐬 𝐝𝐞 𝐨𝐩𝐨𝐫𝐭𝐮𝐧𝐢𝐝𝐚𝐝
◉ ¿Es buen día para operar en long con 3x?
◉ Nivel de entrada ideal y stop técnico con justificación basada en la estructura, momentum y volatilidad.

Usa un lenguaje visual, con estructura clara y negritas 𝐜𝐨𝐦𝐨 𝐞𝐬𝐭𝐚 para títulos. Incluye emoticonos relevantes. Usa gpt-4o.
"""

    response_resumen = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt_resumen}]
    )
    message_resumen = response_resumen.choices[0].message["content"]

    response_extenso = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt_extenso}]
    )
    message_extenso = response_extenso.choices[0].message["content"]

    url_photo = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    url_text = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    for chat_id in [CHANNEL_CHAT_ID_ES, CHANNEL_CHAT_ID_EN]:
        requests.post(url_photo, data={
            "chat_id": chat_id,
            "photo": "https://cryptosignalbot.com/wp-content/uploads/2025/03/21.png"
        })

    payload_resumen = {
        "chat_id": CHANNEL_CHAT_ID_ES,
        "text": message_resumen,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [[{
                "text": "📖 Ver análisis completo",
                "callback_data": "ver_extenso"
            }]]
        }
    }

    payload_extenso = {
        "chat_id": CHANNEL_CHAT_ID_ES,
        "text": message_extenso,
        "parse_mode": "HTML"
    }

    requests.post(url_text, json=payload_resumen)
    requests.post(url_text, json=payload_extenso)

# Para que lo ejecutes tú desde Render o local
# send_prompt_01()
