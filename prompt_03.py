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
    Actúa como un analista técnico profesional especializado en criptomonedas. Tu objetivo es generar un análisis estructurado y preciso del comportamiento de Bitcoin (BTCUSD), enfocado únicamente en operaciones LONG de corto plazo. El análisis se basa en el gráfico de 1 hora, pero debe considerar múltiples temporalidades y factores macroeconómicos El precio actual de BTC es {precio_btc} USD..

    🧠 Utiliza indicadores técnicos como:
    - Velas japonesas
    - EMAs (21, 55, 100, 200)
    - RSI
    - SQZMOM
    - Volumen (POC)
    - Retrocesos de Fibonacci en 1D y 4H (solo para análisis interno, no mostrar en el mensaje)
    
    Además, evalúa eventos macroeconómicos o políticos importantes (FED, CPI, datos de empleo, declaraciones de Trump u otros líderes, conflictos globales, etc.) para reforzar o rechazar la validez de operar hoy.

➡️ Crea un mensaje con estilo motivador, análisis real y visualmente claro para Telegram. El precio actual de BTC es {precio_btc} USD.

Usa esta estructura exacta en el mensaje generado:

¡Buenas noches traders! Qué mejor manera de cerrar el día que con nuestra última señal. Analicemos cómo cerró Bitcoin y lo que se espera para mañana. ¡Vamos allá!

𝐅𝐞𝐜𝐡𝐚: {fecha_hoy}  
𝐒𝐞𝐧̃𝐚𝐥: 3 de 3

Nuestro equipo trabaja arduamente para ofrecer análisis técnico y fundamental en tiempo real tres veces al día, asegurándonos de mantener a nuestra comunidad completamente informada y preparada.

---
📊 → 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐓𝐞́𝐜𝐧𝐢𝐜𝐨:

𝟏. 𝐆𝐫𝐚́𝐟𝐢𝐜𝐨 𝐃𝐢𝐚𝐫𝐢𝐨
Resumen técnico breve con:
• Tendencia general del día

𝟐. 𝐆𝐫𝐚́𝐟𝐢𝐜𝐨 𝐝𝐞 𝟒 𝐇𝐨𝐫𝐚𝐬
Resumen técnico breve con:
• Estructura de velas y dirección dominante
• Zonas clave de rebote o congestión
• Lectura rápida del RSI y volumen

𝟑. 𝐆𝐫𝐚́𝐟𝐢𝐜𝐨 𝐝𝐞 𝟏 𝐇𝐨𝐫𝐚
• Patrones de velas (envolventes, doji, martillo, etc.)
• Soportes y resistencias precisas
• EMAs (21, 55, 100, 200) como soporte/resistencia dinámica
• Retrocesos de Fibonacci relevantes (38.2%, 50%, 61.8%, 78.6%)
• RSI con comentarios de sobrecompra/sobreventa o divergencias
• Volumen con Point of Control y zonas de acumulación/distribución
• SQZMOM para evaluar si hay compresión o expansión y la dirección del momentum

---
🔍 → 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥

Evalúa si hay eventos macroeconómicos, políticos o geopolíticos importantes que puedan afectar el comportamiento de BTC hoy. Entre ellos deben considerarse:

• Reuniones clave como la FED, publicación de datos económicos (CPI, NFP, etc.)
• Movimiento del índice del dólar (DXY)
• Noticias sobre figuras políticas influyentes como **Donald Trump**, decisiones regulatorias, declaraciones oficiales o conflictos internacionales
• Sentimiento general del mercado (acumulación/distribución, narrativa en redes, actividad de ballenas)
• Relación con índices bursátiles como SP500 o Nasdaq si aplica

⚠️ Si hay **noticias de alto impacto o declaraciones políticas que generen incertidumbre significativa**, indica claramente que **no es recomendable operar hoy**, o que la probabilidad es baja. En ese caso, recomienda esperar confirmaciones técnicas.

La información debe ser analizada y utilizada para **calcular la probabilidad final de éxito**, aunque no es necesario listar todas las noticias si no son relevantes. Solo deben mencionarse si tienen impacto directo.

---
🚨 𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧 (𝐋𝐨𝐧𝐠 𝟑𝐱):

Realiza el cálculo completo basándote en el análisis técnico multitemporal y el análisis fundamental del día. Considera especialmente:
• Los retrocesos de Fibonacci en 1D y 4H (como herramienta interna de precisión, no mostrar en el mensaje final)
• La estructura del mercado actual
• El momentum, volumen y zonas de soporte/resistencia clave
• Las noticias macroeconómicas activas

A partir del análisis técnico y fundamental completo, genera un:

💰 𝐏𝐫𝐞𝐜𝐢𝐨 𝐝𝐞 𝐞𝐧𝐭𝐫𝐚𝐝𝐚 𝐨́𝐩𝐭𝐢𝐦𝐨: ajustado al nivel más técnico posible  
🎯 𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧: máximo del 2%, calculado en gráfico de 1 hora  
🟢 𝐏𝐫𝐨𝐛𝐚𝐛𝐢𝐥𝐢𝐝𝐚𝐝 𝐝𝐞 𝐞𝐱𝐢𝐭𝐨 𝐞𝐬𝐭𝐢𝐦𝐚𝐝𝐚: resultado (%) del análisis técnico + fundamental

Si la probabilidad es superior al 70%, indica:

🔁 𝐄𝐬 𝐮𝐧𝐚 𝐨𝐩𝐨𝐫𝐭𝐮𝐧𝐢𝐝𝐚𝐝 𝐝𝐞 𝐚𝐥𝐭𝐚 𝐩𝐫𝐞𝐜𝐢𝐬𝐢𝐨́𝐧.  
𝐋𝐚 𝐦𝐞𝐣𝐨𝐫 𝐞𝐬𝐭𝐫𝐚𝐭𝐞𝐠𝐢𝐚 𝐞𝐬 𝐢𝐫 𝐚𝐛𝐫𝐢𝐞𝐧𝐝𝐨 𝐲 𝐜𝐞𝐫𝐫𝐚𝐧𝐝𝐨 𝐩𝐨𝐬𝐢𝐜𝐢𝐨𝐧𝐞𝐬 𝐜𝐨𝐫𝐭𝐚𝐬 𝐝𝐞𝐧𝐭𝐫𝐨 𝐝𝐞𝐥 𝐫𝐚𝐧𝐠𝐨 𝐝𝐢𝐚𝐫𝐢𝐨.  
𝐀𝐩𝐫𝐨𝐯𝐞𝐜𝐡𝐚 𝐥𝐨𝐬 𝐢𝐦𝐩𝐮𝐥𝐬𝐨𝐬 𝐲 𝐥𝐚 𝐜𝐨𝐧𝐬𝐨𝐥𝐢𝐝𝐚𝐜𝐢𝐨́𝐧.

𝐒𝐢 𝐥𝐚 𝐩𝐫𝐨𝐛𝐚𝐛𝐢𝐥𝐢𝐝𝐚𝐝 𝐞𝐬 𝐛𝐚𝐣𝐚 (<70%), indica claramente:

⚠️ 𝐄𝐧 𝐞𝐬𝐭𝐞 𝐦𝐨𝐦𝐞𝐧𝐭𝐨 𝐧𝐨 𝐡𝐚𝐲 𝐮𝐧𝐚 𝐨𝐩𝐨𝐫𝐭𝐮𝐧𝐢𝐝𝐚𝐝 𝐜𝐥𝐚𝐫𝐚 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧.  
𝐋𝐚𝐬 𝐜𝐨𝐧𝐝𝐢𝐜𝐢𝐨𝐧𝐞𝐬 𝐚𝐜𝐭𝐮𝐚𝐥𝐞𝐬 𝐧𝐨 𝐬𝐨𝐧 𝐟𝐚𝐯𝐨𝐫𝐚𝐛𝐥𝐞𝐬 𝐲 𝐥𝐚 𝐩𝐫𝐨𝐛𝐚𝐛𝐢𝐥𝐢𝐝𝐚𝐝 𝐝𝐞 𝐞𝐱𝐢𝐭𝐨 𝐞𝐬 𝐛𝐚𝐣𝐚.  
📌 𝐒𝐞 𝐫𝐞𝐜𝐨𝐦𝐢𝐞𝐧𝐝𝐚 𝐞𝐬𝐩𝐞𝐫𝐚𝐫 𝐞𝐥 𝐚𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐝𝐞 𝐦𝐢𝐭𝐚𝐝 𝐝𝐞 𝐬𝐞𝐬𝐢𝐨́𝐧 𝐩𝐚𝐫𝐚 𝐨𝐛𝐭𝐞𝐧𝐞𝐫 𝐜𝐨𝐧𝐟𝐢𝐫𝐦𝐚𝐜𝐢𝐨𝐧𝐞𝐬 𝐦𝐚́𝐬 𝐬𝐨́𝐥𝐢𝐝𝐚𝐬.

Ejemplo del formato a entregar:

🚨 𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧 (𝐋𝐨𝐧𝐠 𝟑𝐱):

💰 Entrada óptima entre: ${rango_min}  
🎯𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧: Entre ${rango_min} – ${rango_max}  
🟢 Porcentaje de efectividad estimado: {efectividad}%  
Condiciones ideales para una operación intradía de alta probabilidad.  
⚠️ ¡Cuida tu gestión de riesgo! No te olvides de establecer una estrategia de salida. Este mercado es altamente volátil.//

---
🎁 𝐏𝐮𝐞𝐝𝐞𝐬 𝐮𝐧𝐢𝐫𝐭𝐞 𝐚 𝐧𝐮𝐞𝐬𝐭𝐫𝐚 𝐳𝐨𝐧𝐚 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐒𝐞𝐧̃𝐚𝐥𝐞𝐬 𝐝𝐞 𝐓𝐫𝐚𝐝𝐢𝐧𝐠 𝐜𝐨𝐧 𝐄́𝐱𝐢𝐭𝐨 𝐆𝐚𝐫𝐚𝐧𝐭𝐢𝐳𝐚𝐝𝐨:

🔥 𝐅𝐈𝐑𝐄 𝐒𝐜𝐚𝐥𝐩𝐢𝐧𝐠  
🏅 Rendimiento: 85.64%  
🟢 Ganadoras: 1,563  
🔴 Perdedoras: 262  

💎 𝐄𝐋𝐈𝐓𝐄 𝐒𝐜𝐚𝐥𝐩𝐢𝐧𝐠 𝐏𝐑𝐎  
🏅 Rendimiento: 99.10%  
🟢 Ganadoras: 552  
🔴 Perdedoras: 5  

🪙 𝐃𝐄𝐋𝐓𝐀 𝐒𝐰𝐢𝐧𝐠  
🏅 Rendimiento: 96.00% 
🟢 Ganadoras: 48  
🔴 Perdedoras: 2 

• Señales en tiempo real enviadas directo a nuestro sitio web y Telegram  
• Historial público de operaciones para verificar resultados reales  
• Plataforma con gráficos en vivo y seguimiento al mercado  
• Noticias, calendario económico y análisis en vivo cada día
• Soporte 24/7 para responder tus dudas 
--- 

✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨ Mantente pendiente del mensaje de mitad de sesión. ¡Feliz trading!
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

    url_photo = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    url_msg = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    imagen_url = "https://cryptosignalbot.com/wp-content/uploads/2025/03/fin-ses.png"

    # Primero enviamos la imagen a ambos canales
    for canal in [CHANNEL_CHAT_ID_ES, CHANNEL_CHAT_ID_EN]:
        requests.post(url_photo, data={"chat_id": canal, "photo": imagen_url})

    # Luego el mensaje con botón
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
        requests.post(url_msg, json=payload)
