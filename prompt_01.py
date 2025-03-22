import os
import requests
import openai
from datetime import datetime
import random

# Asegúrate de que las variables de entorno OPENAI_API_KEY y TELEGRAM_BOT_TOKEN
# estén definidas en tu entorno. Ejemplo en terminal (Linux/Mac):
# export OPENAI_API_KEY="tu_clave_openai"
# export TELEGRAM_BOT_TOKEN="tu_token_telegram"

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Reemplaza con tu canal de Telegram (en español)
CHANNEL_CHAT_ID_ES = "-1002440626725"  # Por ejemplo

def obtener_fecha_en_espanol():
    """Devuelve la fecha en el formato 'día de mes de año' en español."""
    meses = {
        "January": "enero", "February": "febrero", "March": "marzo",
        "April": "abril", "May": "mayo", "June": "junio",
        "July": "julio", "August": "agosto", "September": "septiembre",
        "October": "octubre", "November": "noviembre", "December": "diciembre"
    }
    hoy = datetime.now()
    mes = meses[hoy.strftime("%B")]
    return f"{hoy.day} de {mes} de {hoy.year}"

def obtener_precio_bitcoin():
    """
    Consulta la API de CoinGecko para obtener el precio aproximado de Bitcoin en USD.
    Retorna el precio como float. 
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        return data["bitcoin"]["usd"]
    except Exception:
        # En caso de error, usar un valor por defecto
        return 28000.0

def generar_indicadores_tecnicos(precio_actual):
    """
    Genera datos hipotéticos/aleatorios para RSI, POC, etc.
    Puedes adaptar esto para calcular realmente los indicadores 
    o usar otra API si lo deseas.
    """
    # Ejemplo de RSI aleatorio entre 30 y 70
    rsi_valor = random.uniform(30, 70)
    # Suponiendo un rango de 2% alrededor del precio actual
    rango_inferior = precio_actual * 0.98
    rango_superior = precio_actual * 1.02

    # Simular brevemente cada indicador
    indicadores = {
        "velas": "Patrón de velas alcistas con ligera corrección",
        "emas": "Las EMAs indican soporte clave en la zona de corto plazo",
        "fibonacci": "Respeto del nivel 0.382 con posible rebote",
        "poc": "Acumulación moderada, indicando presión de compra",
        "rsi": f"{rsi_valor:.2f} (nivel neutro a ligeramente alcista)",
        "sqzmom": "SQZMOM con momentum en expansión"
    }
    return indicadores, rango_inferior, rango_superior

def send_prompt_01():
    # 1) Obtenemos la fecha
    fecha = obtener_fecha_en_espanol()
    # 2) Obtenemos el precio de Bitcoin
    precio_btc = obtener_precio_bitcoin()
    # 3) Generamos indicadores técnicos "simulados"
    indicadores, rango_inferior, rango_superior = generar_indicadores_tecnicos(precio_btc)

    # 4) Construimos el PROMPT para GPT-4 (o el modelo que tengas disponible)
    prompt_es = f"""
Actúa como un analista técnico profesional de criptomonedas. 
Genera un mensaje para Telegram (en español) dirigido a traders, 
con datos reales (o mínimos) e indicadores de mercado, en este formato exacto:

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
📊 Velas: {indicadores["velas"]}
📈 EMAs: {indicadores["emas"]}
🔁 Fibonacci: {indicadores["fibonacci"]}
🧱 POC: {indicadores["poc"]}
⚡️ RSI: {indicadores["rsi"]}
🚀 SQZMOM: {indicadores["sqzmom"]}

◉ 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥:
💵 DXY: El índice del dólar muestra leve fluctuación, generando volatilidad en BTC.
🧠 Sentimiento: Predominantemente alcista, aunque con cautela.
📈 Nasdaq/SP500: Correlación moderada, reflejando un mercado mixto.

◉ 𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧 (𝐋𝐨𝐧𝐠 𝟑𝐱):
💰 Entrada óptima entre: ${rango_inferior:,.2f} y ${rango_superior:,.2f}
🎯𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧: Entre ${rango_inferior:,.2f} y ${rango_superior:,.2f}
🟢 Porcentaje de efectividad estimado: 68%
Condiciones ideales para una operación intradía de alta probabilidad.
⚠️ ¡Cuida tu gestión de riesgo! Este mercado es altamente volátil. Operación válida solo para hoy.

📊 Señales, gráficos en vivo y análisis en tiempo real completamente GRATIS por 30 días.
🔑 𝐎𝐛𝐭𝐞́𝐧 𝐭𝐮 𝐦𝐞𝐬 𝐠𝐫𝐚𝐭𝐢𝐬 𝐚𝐡𝐨𝐫𝐚! 🚀

Gracias por elegirnos como tu portal de trading de confianza. ¡Juntos, haremos que tu inversión crezca!
✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨Mantente pendiente del mensaje de mitad de sesión. ¡Feliz trading!
"""

    # 5) Llamada a OpenAI para obtener el mensaje final
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Ajusta al modelo que desees, por ejemplo: "gpt-3.5-turbo"
        messages=[
            {"role": "user", "content": prompt_es}
        ]
    )

    # 6) Tomamos el contenido generado
    mensaje_es = response.choices[0].message["content"].strip()

    # 7) Enviamos el mensaje a Telegram
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

if __name__ == "__main__":
    send_prompt_01()

    # Si deseas activarlo también para el canal en inglés, lo agregamos luego con su propio prompt_en.
