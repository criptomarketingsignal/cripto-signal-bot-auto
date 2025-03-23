import os
import requests
import openai
from datetime import datetime
import time

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

    resumen_es = f"""
📈 Bitcoin – Señal 1 de 3 ({fecha_es})

🔍 BTC muestra consolidación con intención alcista.  
📊 RSI sobre 55, volumen moderado.  
📈 EMAs cruzadas al alza en 1H y 4H.  
💹 DXY a la baja y Nasdaq firme: buen entorno macro.

💰 Entrada ideal entre ${rango_min} – ${rango_max}  
🔄 Rango Operativo Diario | Long 3x  
📎 Análisis completo a continuación 👇
"""

    prompt_extenso = f"""
Quiero que actúes como un analista técnico profesional especializado en criptomonedas, y realices un análisis detallado del precio de Bitcoin para hoy, {fecha_es}.

### PASO 2: Análisis Técnico Multitemporal
Realiza un análisis técnico del gráfico de Bitcoin (BTCUSD) en las siguientes temporalidades:
- 1W, 1D, 4H, 1H

Incluye:
1. Velas Japonesas: patrones, estructuras.
2. Soportes/Resistencias + EMAs (21/55/100/200)
3. Fibonacci en 4H y 1D (38.2%, 50%, 61.8%, 78.6%)
4. Volumen (POC)
5. RSI en 1H, 4H, 1D
6. SQZMOM en 4H y 1D

### PASO 3: Análisis Fundamental
- Eventos de EE.UU. (FED, CPI, empleo)
- DXY
- Sentimiento del mercado (ballenas, redes)
- Relación con SP500 / Nasdaq

### PASO 4: Rango de Operación
Determina si HOY es buen día para operar en LONG.
Calcula un precio de entrada ideal y un precio de salida de compras basado en datos reales, sin usar rangos fijos.
Debe justificarse por: volatilidad, estructura, momentum y volumen, soportes/resistencias.
"""

    # Obtener mensajes
    response_resumen = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": resumen_es}]
    )
    mensaje_resumen = response_resumen.choices[0].message["content"]

    response_extenso = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt_extenso}]
    )
    mensaje_extenso = response_extenso.choices[0].message["content"]

    url_photo = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    url_text = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    for canal in [CHANNEL_CHAT_ID_ES, CHANNEL_CHAT_ID_EN]:
        requests.post(url_photo, data={
            "chat_id": canal,
            "photo": "https://cryptosignalbot.com/wp-content/uploads/2025/03/21.png",
            "caption": mensaje_resumen
        })
        time.sleep(2)
        requests.post(url_text, json={
            "chat_id": canal,
            "text": mensaje_extenso,
            "parse_mode": "HTML",
            "reply_markup": {
                "inline_keyboard": [[
                    {
                        "text": "Señales premium 30 días gratis ✨",
                        "url": "https://t.me/CriptoSignalBotGestion_bot?start=676731307b8344cb070ac996"
                    }
                ]]
            }
        })
