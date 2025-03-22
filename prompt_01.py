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

    # Prompt en español
    prompt_es = f"""
Actúa como un analista técnico profesional especializado en criptomonedas y genera un mensaje en español perfectamente estructurado para el canal de señales.

➡️ El análisis debe estar enfocado en una operación de tipo LONG, con apalancamiento 3x, y válido solo para el día de hoy.

➡️ Calcula un rango de operación (entrada) para hoy basado en el precio actual real de BTC (usa el que tú ves). Si no hay condiciones técnicas favorables claras, indica que NO se recomienda operar hoy y no proporciones un rango.

➡️ Usa un tono motivador, con análisis realista, y visualmente claro para Telegram. Formatea con este estilo: negritas en unicode (𝐞𝐬𝐭𝐞 𝐭𝐢𝐩𝐨), emojis, y viñetas ◉.

𝐌𝐨𝐝𝐞𝐥𝐨 𝐝𝐞 𝐦𝐞𝐧𝐬𝐚𝐣𝐞:

Buenos días traders! ¿Están listos para nuestra primera señal del día? Hoy vamos a dejar nuestras huellas en el mundo del Bitcoin. ¡Preparen sus gráficos!

𝐅𝐞𝐜𝐡𝐚: {fecha}  
𝐒𝐞𝐧̃𝐚𝐥: 1 de 3 

Somos un equipo comprometido a proporcionarte el análisis técnico y fundamental más reciente, tres veces al día para que siempre estés actualizado y preparado para tomar decisiones precisas.

Herramientas que utilizamos:
- Velas japonesas 📊  
- Medias Móviles Exp 📈  
- Fibonacci 🔢  
- Fuerza Relativa (RSI) ⚖️  
- SQZMOM (Momentum Squeeze) ⚡️  
- Volumen (POC) 💼

◉ 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐓𝐞́𝐜𝐧𝐢𝐜𝐨:  
Incluye un análisis basado en RSI, EMA, Fibonacci, SQZMOM, POC y velas.

◉ 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥:  
Incluye visión del DXY, sentimiento de mercado y Nasdaq/SP500.

◉ 𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧 (𝐋𝐨𝐧𝐠 𝟑𝐱):  
💰 Entrada óptima: Calcula el rango exacto más favorable  
🟢 Probabilidad de éxito: muy precisa, basada en indicadores  
⚠️ Cuida tu gestión de riesgo, operación solo para hoy

📊 Señales, gráficos en vivo y análisis en tiempo real completamente GRATIS por 30 días.  
🔑 𝐎𝐛𝐭𝐞́𝐧 𝐭𝐮 𝐦𝐞𝐬 𝐠𝐫𝐚𝐭𝐢𝐬 𝐚𝐡𝐨𝐫𝐚! 🚀

Muchas gracias por confiar en nosotros como tu portal de trading. Juntos haremos crecer tu inversión.  
✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨ Estén atentos para el 2º mensaje (mitad de sesión, Hora de Nueva York). ¡Feliz trading!
"""

    prompt_en = f"""
Act as a professional technical analyst specialized in cryptocurrencies and create a well-structured message in English for our signal channel.

➡️ The analysis must be for a LONG trade, with 3x leverage, valid only for today.

➡️ Calculate a realistic and actionable entry range for today using the actual BTC price (the one you see). If there are no favorable conditions, clearly state that no long trade is recommended today.

➡️ The tone must be clear, motivational and formatted for Telegram: bold in unicode (𝐭𝐡𝐢𝐬 𝐬𝐭𝐲𝐥𝐞), bullet points ◉ and emojis.

Structure the message similar to the Spanish format.
"""

    # Solicita a OpenAI el mensaje en español
    response_es = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt_es}]
    )
    mensaje_es = response_es.choices[0].message["content"]

    # Solicita a OpenAI el mensaje en inglés
    response_en = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt_en}]
    )
    mensaje_en = response_en.choices[0].message["content"]

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    # Enviar al canal en español
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

    # Enviar al canal en inglés
    payload_en = {
        "chat_id": CHANNEL_CHAT_ID_EN,
        "text": mensaje_en,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "Free 30-Day Premium Access ✨",
                        "url": "https://t.me/CriptoSignalBotGestion_bot?start=676731307b8344cb070ac996"
                    }
                ]
            ]
        }
    }
    requests.post(url, json=payload_en)
