import os
import requests
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_CHAT_ID_ES = "-1001234567890"  # Reemplaza con el ID/usuario de tu canal ES
CHANNEL_CHAT_ID_EN = "-1009876543210"  # Reemplaza con el ID/usuario de tu canal EN

def obtener_fecha_es():
    """
    Devuelve la fecha en español: Ej. '24 de marzo de 2025'
    """
    meses = {
        "January": "enero", "February": "febrero", "March": "marzo",
        "April": "abril", "May": "mayo", "June": "junio",
        "July": "julio", "August": "agosto", "September": "septiembre",
        "October": "octubre", "November": "noviembre", "December": "diciembre"
    }
    hoy = datetime.now()
    mes_es = meses[hoy.strftime("%B")]
    return f"{hoy.day} de {mes_es} de {hoy.year}"

def obtener_fecha_en():
    """
    Devuelve la fecha en inglés: Ej. 'March 24, 2025'
    """
    return datetime.now().strftime("%B %d, %Y")

def obtener_precio_btc():
    """
    Devuelve el precio de Bitcoin (BTC) en USD consultando CoinGecko.
    Retorna None si ocurre un error.
    """
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": "bitcoin", "vs_currencies": "usd"}
        r = requests.get(url, params=params)
        data = r.json()
        return float(data["bitcoin"]["usd"])
    except Exception as e:
        print("Error al obtener precio de BTC:", e)
        return None

def calcular_rangos(precio):
    """
    Cálculo simple de rango para ejemplo.
    Retorna (rango_min, rango_max, efectividad).
    """
    rango_min = round(precio * 0.9925, 2)
    rango_max = round(precio * 1.0025, 2)
    # Efectividad “ficticia”
    efectividad = round(98.5, 2)
    return rango_min, rango_max, efectividad

def send_prompt_01():
    """
    Envía dos señales:
    1) Un primer mensaje con imagen + caption (ES e INGLÉS), ~<950 caracteres
    2) Un segundo mensaje "extenso" (ES e INGLÉS), empezando desde PASO 2
    """
    fecha_es = obtener_fecha_es()
    fecha_en = obtener_fecha_en()
    precio = obtener_precio_btc()
    if not precio:
        print("No se pudo obtener el precio de BTC. Saliendo.")
        return

    rango_min, rango_max, efectividad = calcular_rangos(precio)

    # --- PRIMER MENSAJE - ES ---
    primer_mensaje_es = (
        f"Buenos días traders ✨!\n"
        f"Hoy analizamos Bitcoin (BTC). ¡Vamos allá! 🚀\n"
        f"𝐅𝐞𝐜𝐡𝐚: {fecha_es}\n"
        f"𝐏𝐫𝐞𝐜𝐢𝐨 𝐁𝐓𝐂: ${precio}\n\n"
        f"◉ Rango Long 3x:\n"
        f"Entrada: ${rango_min}\n"
        f"Hasta: ${rango_max}\n"
        f"Eficiencia: {efectividad}%\n\n"
        f"Recomendación intradía (stop 60%).\n"
        f"🔑 𝐎𝐛𝐭𝐞́𝐧 𝐭𝐮 𝐦𝐞𝐬 𝐠𝐫𝐚𝐭𝐢𝐬 𝐚𝐪𝐮𝐢́ 👇"
    )

    # --- PRIMER MENSAJE - EN ---
    primer_mensaje_en = (
        f"Good morning traders ✨!\n"
        f"Today we analyze Bitcoin (BTC). Let's go! 🚀\n"
        f"𝐃𝐚𝐭𝐞: {fecha_en}\n"
        f"𝐁𝐓𝐂 𝐏𝐫𝐢𝐜𝐞: ${precio}\n\n"
        f"◉ Long 3x Range:\n"
        f"Entry: ${rango_min}\n"
        f"Up to: ${rango_max}\n"
        f"Efficiency: {efectividad}%\n\n"
        f"Intraday recommendation (60% stop).\n"
        f"🔑 𝐂𝐥𝐚𝐢𝐦 𝐲𝐨𝐮𝐫 𝐅𝐑𝐄𝐄 𝐦𝐨𝐧𝐭𝐡 👇"
    )

    # Imagen que se enviará en ambos
    image_url = "https://cryptosignalbot.com/wp-content/uploads/2025/03/21.png"

    # Inline keyboard (botón) - Español
    keyboard_es = {
        "inline_keyboard": [[
            {
                "text": "Señales premium 30 días gratis ✨",
                "url": "https://t.me/CriptoSignalBotGestion_bot?start=xxxx"
            }
        ]]
    }
    # Inline keyboard (botón) - Inglés
    keyboard_en = {
        "inline_keyboard": [[
            {
                "text": "Free Premium Signals 30 Days ✨",
                "url": "https://t.me/CriptoSignalBotGestion_bot?start=xxxx"
            }
        ]]
    }

    # Enviar primer mensaje (imagen + caption) ES
    url_photo = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    requests.post(
        url_photo,
        data={
            "chat_id": CHANNEL_CHAT_ID_ES,
            "photo": image_url,
            "caption": primer_mensaje_es,
            "parse_mode": "HTML",
        },
        json={
            "reply_markup": keyboard_es
        }
    )

    # Enviar primer mensaje (imagen + caption) EN
    requests.post(
        url_photo,
        data={
            "chat_id": CHANNEL_CHAT_ID_EN,
            "photo": image_url,
            "caption": primer_mensaje_en,
            "parse_mode": "HTML",
        },
        json={
            "reply_markup": keyboard_en
        }
    )

    # --- SEGUNDO MENSAJE: Análisis extenso (PASO 2 en adelante) ---
    analisis_extenso_es = f"""
𝐏𝐀𝐒𝐎 𝟐: 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐓𝐞́𝐜𝐧𝐢𝐜𝐨 𝐌𝐮𝐥𝐭𝐢𝐭𝐞𝐦𝐩𝐨𝐫𝐚𝐥
◉ Revisar 1W, 1D, 4H, 1H (velas, EMAs, Fibonacci, POC, RSI, SQZMOM)

𝐏𝐀𝐒𝐎 𝟑: 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥
◉ FED, CPI, DXY, sentimiento de mercado, correlaciones

𝐏𝐀𝐒𝐎 𝟒: 𝐒𝐞𝐧̃𝐚𝐥 𝐝𝐞 𝐓𝐫𝐚𝐝𝐢𝐧𝐠
◉ Determinar si hoy es propicio un Long 3x (stop 60%)
◉ Precio de entrada y stop dinámicos (soportes/resistencias, momentum)

¡Lista la estructura de tu operativa BTC! 🎯
"""

    analisis_extenso_en = f"""
𝐒𝐓𝐄𝐏 𝟐: 𝐌𝐮𝐥𝐭𝐢-𝐓𝐢𝐦𝐞𝐟𝐫𝐚𝐦𝐞 𝐓𝐞𝐜𝐡𝐧𝐢𝐜𝐚𝐥 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬
◉ Review 1W, 1D, 4H, 1H (candles, EMAs, Fibonacci, POC, RSI, SQZMOM)

𝐒𝐓𝐄𝐏 𝟑: 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬
◉ FED, CPI, DXY, market sentiment, correlations

𝐒𝐓𝐄𝐏 𝟒: 𝐓𝐫𝐚𝐝𝐢𝐧𝐠 𝐒𝐢𝐠𝐧𝐚𝐥
◉ Decide if a 3x Long is good today (60% stop)
◉ Dynamic entry & stop (support/resistance, momentum)

Here is your BTC trading framework! 🎯
"""

    # (Opcional) Embellecer con GPT-4o
    try:
        resp_es = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": analisis_extenso_es}],
            max_tokens=700,
            temperature=0.7
        )
        analisis_extenso_es = resp_es.choices[0].message["content"]
    except Exception as e:
        print("Error GPT-4o en ES:", e)

    try:
        resp_en = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": analisis_extenso_en}],
            max_tokens=700,
            temperature=0.7
        )
        analisis_extenso_en = resp_en.choices[0].message["content"]
    except Exception as e:
        print("Error GPT-4o en EN:", e)

    # Enviar segundo mensaje (texto) ES
    url_text = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url_text, json={
        "chat_id": CHANNEL_CHAT_ID_ES,
        "text": analisis_extenso_es,
        "parse_mode": "HTML",
        "reply_markup": keyboard_es
    })

    # Enviar segundo mensaje (texto) EN
    requests.post(url_text, json={
        "chat_id": CHANNEL_CHAT_ID_EN,
        "text": analisis_extenso_en,
        "parse_mode": "HTML",
        "reply_markup": keyboard_en
    })

# Si deseas ejecutar directamente en Render o local:
if __name__ == "__main__":
    send_prompt_01()
