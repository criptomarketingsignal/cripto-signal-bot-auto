import os
import requests
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_CHAT_ID_ES = "-1001234567890"  # Reemplaza con tu canal/ID en español
CHANNEL_CHAT_ID_EN = "-1009876543210"  # Reemplaza con tu canal/ID en inglés

# --- Funciones Auxiliares ---
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

# --- Función Principal ---
def enviar_senales():
    # Obtener datos básicos
    fecha_es = obtener_fecha_es()
    fecha_en = obtener_fecha_en()
    precio = obtener_precio_btc()
    if not precio:
        print("No se pudo obtener el precio de BTC. Saliendo.")
        return

    rango_min, rango_max, efectividad = calcular_rangos(precio)

    # PRIMER MENSAJE (con imagen) - Español
    # Debe ser <= 950 caracteres
    # Añadimos inline keyboard en 'sendPhoto' via 'reply_markup'
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

    # PRIMER MENSAJE (con imagen) - Inglés
    # También <= 950 caracteres
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

    # Imagen que se enviará
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

    # 1) Enviar foto+caption a canal ES
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

    # 2) Enviar foto+caption a canal EN
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

    # SEGUNDO MENSAJE: ANÁLISIS EXTENSO (ya no limitado a 950 chars)
    # Comienza desde PASO 2 en adelante. Lo generamos en ES y EN.

    analisis_extenso_es = f"""
𝐏𝐀𝐒𝐎 𝟐: 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐓𝐞́𝐜𝐧𝐢𝐜𝐨 𝐌𝐮𝐥𝐭𝐢𝐭𝐞𝐦𝐩𝐨𝐫𝐚𝐥
◉ Revisa 1W, 1D, 4H, 1H (velas japonesas, soportes/resistencias con EMAs, retrocesos Fibonacci, volumen POC, RSI, SQZMOM).

𝐏𝐀𝐒𝐎 𝟑: 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥
◉ Eventos macro (FED, CPI, DXY).
◉ Sentimiento de mercado, correlación SP500/Nasdaq.

𝐏𝐀𝐒𝐎 𝟒: 𝐃𝐞𝐭𝐞𝐫𝐦𝐢𝐧𝐚𝐫 𝐥𝐚 𝐒𝐞𝐧̃𝐚𝐥
◉ ¿Hoy es propicio un Long 3x? Stop máximo 60%, intradía.
◉ Define precio de entrada y stop basado en soportes, resistencias y momentum.

¡Listo! Con esto tienes la estructura esencial para tu operativa de Bitcoin. 🎯
"""

    analisis_extenso_en = f"""
𝐒𝐓𝐄𝐏 𝟐: 𝐌𝐮𝐥𝐭𝐢-𝐓𝐢𝐦𝐞𝐟𝐫𝐚𝐦𝐞 𝐓𝐞𝐜𝐡𝐧𝐢𝐜𝐚𝐥 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬
◉ Review 1W, 1D, 4H, 1H (candlesticks, support/resistance with EMAs, Fibonacci, POC volume, RSI, SQZMOM).

𝐒𝐓𝐄𝐏 𝟑: 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬
◉ Macro events (FED, CPI, DXY).
◉ Market sentiment, SP500/Nasdaq correlation.

𝐒𝐓𝐄𝐏 𝟒: 𝐓𝐫𝐚𝐝𝐢𝐧𝐠 𝐒𝐢𝐠𝐧𝐚𝐥
◉ Consider a 3x Long? Max 60% stop, intraday.
◉ Entry/stop levels based on support, resistance, momentum.

That's it! Here you have the essential structure for your Bitcoin strategy. 🎯
"""

    # Embellecer los textos extensos con GPT-4o (opcional)
    try:
        resp_es = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": analisis_extenso_es}],
            temperature=0.7,
            max_tokens=700
        )
        analisis_extenso_es = resp_es.choices[0].message["content"]
    except Exception as e:
        print("Error GPT-4o ES:", e)

    try:
        resp_en = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": analisis_extenso_en}],
            temperature=0.7,
            max_tokens=700
        )
        analisis_extenso_en = resp_en.choices[0].message["content"]
    except Exception as e:
        print("Error GPT-4o EN:", e)

    # Enviar segundo mensaje (texto) en ambos canales
    url_text = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    # Español
    payload_es = {
        "chat_id": CHANNEL_CHAT_ID_ES,
        "text": analisis_extenso_es,
        "parse_mode": "HTML",
        "reply_markup": keyboard_es
    }
    requests.post(url_text, json=payload_es)

    # Inglés
    payload_en = {
        "chat_id": CHANNEL_CHAT_ID_EN,
        "text": analisis_extenso_en,
        "parse_mode": "HTML",
        "reply_markup": keyboard_en
    }
    requests.post(url_text, json=payload_en)


# Si deseas ejecutarlo directamente:
if __name__ == "__main__":
    enviar_senales()
