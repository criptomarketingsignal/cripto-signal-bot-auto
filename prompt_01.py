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

    # Prompt en español (actualizado para forzar rango)
    prompt_es = f"""
Actúa como un analista técnico profesional especializado en criptomonedas y genera un mensaje en español perfectamente estructurado para el canal de señales de Telegram.

✅ Debes generar un análisis completo de Bitcoin (BTCUSD) para el día de hoy: {fecha}.

✅ El enfoque es para operaciones LONG con apalancamiento 3x y válido solo por el día actual.

✅ Siempre debes calcular un rango de operación para hoy basado en el precio real actual de BTC. Si las condiciones son difíciles, incluye una advertencia, pero el rango siempre debe estar presente.

✅ Usa tono motivador, directo y visualmente claro para Telegram. Usa negritas en unicode (𝐞𝐬𝐭𝐞 𝐭𝐢𝐩𝐨), viñetas ◉ y emoticonos. Nada de formato Markdown.

Estructura del mensaje generado:

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

    # Prompt en inglés (también con rango obligatorio)
    prompt_en = f"""
Act as a professional crypto analyst and generate a perfectly structured message in English for the Telegram signal channel.

✅ This is a long (3x) operation setup for Bitcoin (BTCUSD), only valid today: {fecha}.

✅ Always calculate a realistic entry range for today based on the actual BTC price. If market conditions are unstable, include a warning, but NEVER skip the range.

✅ Use motivational tone, clear formatting, unicode bold (𝐥𝐢𝐤𝐞 𝐭𝐡𝐢𝐬), bullet points ◉ and emojis. No Markdown.

The structure should follow the same format as the Spanish message.
"""

    # Generar análisis en español
    response_es = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt_es}]
    )
    mensaje_es = response_es.choices[0].message["content"]

    # Generar análisis en inglés
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
            "inline_keyboard": [[
                {
                    "text": "Señales premium 30 días gratis ✨",
                    "url": "https://t.me/CriptoSignalBotGestion_bot?start=676731307b8344cb070ac996"
                }
            ]]
        }
    }
    requests.post(url, json=payload_es)

    # Enviar al canal en inglés
    payload_en = {
        "chat_id": CHANNEL_CHAT_ID_EN,
        "text": mensaje_en,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [[
                {
                    "text": "Free 30-Day Premium Access ✨",
                    "url": "https://t.me/CriptoSignalBotGestion_bot?start=676731307b8344cb070ac996"
                }
            ]]
        }
    }
    requests.post(url, json=payload_en)
