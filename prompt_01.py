from datetime import datetime
import requests
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_CHAT_ID_ES = "-1002440626725"

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

    prompt = f"""
Actúa como un analista técnico profesional especializado en criptomonedas y genera un mensaje en español perfectamente estructurado para el canal de señales.

➡️ Crea un mensaje con estilo motivador, análisis real y visualmente claro para Telegram. El precio actual de BTC es el que tú puedes analizar en tiempo real.

Usa esta estructura exacta en el mensaje generado:

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
🎯 Objetivo de ganancia: nivel técnico realista  
🟢 Probabilidad de éxito: muy precisa, basada en indicadores  
⚠️ Cuida tu gestión de riesgo, operación solo para hoy

📊 Señales, gráficos en vivo y análisis en tiempo real completamente GRATIS por 30 días.  
🔑 𝐎𝐛𝐭𝐞́𝐧 𝐭𝐮 𝐦𝐞𝐬 𝐠𝐫𝐚𝐭𝐢𝐬 𝐚𝐡𝐨𝐫𝐚! 🚀  

Muchas gracias por confiar en nosotros como tu portal de trading. Juntos haremos crecer tu inversión.  
✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨ Estén atentos para el 2º mensaje (mitad de sesión, Hora de Nueva York). ¡Feliz trading!
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    mensaje = response.choices[0].message["content"]

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_CHAT_ID_ES,
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

