from datetime import datetime
import requests
import openai
import os

# Asigna tus claves de API desde variables de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# IDs de los canales en Telegram
CHANNEL_CHAT_ID_ES = "-1002440626725"
CHANNEL_CHAT_ID_EN = "-1002288256984"

def obtener_fecha_en_espanol():
    """Retorna la fecha actual en español, p. ej.: '23 de marzo de 2025'."""
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
    """
    Obtiene el precio actual de BTC en USDT desde la API pública de Binance.
    Devuelve un float con el precio.
    """
    try:
        binance_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(binance_url)
        data = response.json()
        return float(data["price"])
    except Exception as e:
        print("Error al obtener el precio de BTC:", e)
        # En caso de error, puedes devolver un valor por defecto o manejarlo de otra forma
        return 0.0

def send_prompt_01():
    """
    Envía dos mensajes a los canales de Telegram:
      1) Análisis en español.
      2) Análisis en inglés.
    Incluye el precio real de BTC en cada prompt para que GPT-4 genere
    un rango de operación más preciso y contextualizado al día.
    """

    fecha = obtener_fecha_en_espanol()
    precio_btc = obtener_precio_btc()

    # Prompt en español: se incluye el precio actual para el análisis
    prompt_es = f"""
Actúa como un analista técnico profesional especializado en criptomonedas y genera un mensaje en español perfectamente estructurado para el canal de señales de Telegram.

✅ Debes generar un análisis completo de Bitcoin (BTCUSD) para el día de hoy: {fecha}.
✅ El enfoque es para operaciones LONG con apalancamiento 3x y válido solo por el día actual.
✅ El precio actual aproximado de BTC es: {precio_btc:.2f} USDT.
✅ Siempre debes calcular un rango de operación para hoy basado en este precio real de BTC. 
   Si las condiciones son difíciles, incluye una advertencia, pero el rango siempre debe estar presente.
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

    # Prompt en inglés: también incluye el precio actual
    prompt_en = f"""
Act as a professional crypto analyst and generate a perfectly structured message in English for the Telegram signal channel.

✅ This is a long (3x) operation setup for Bitcoin (BTCUSD), only valid today: {fecha}.
✅ The current BTC price is approximately {precio_btc:.2f} USDT.
✅ Always calculate a realistic entry range for today based on this actual BTC price. 
   If market conditions are unstable, include a warning, but NEVER skip the range.
✅ Use a motivational tone, clear formatting, unicode bold (𝐥𝐢𝐤𝐞 𝐭𝐡𝐢𝐬), bullet points ◉ and emojis. No Markdown.

Follow the same structure as the Spanish message. 
"""

    # Llamadas a GPT-4 para generar el análisis en español
    response_es = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt_es}]
    )
    mensaje_es = response_es.choices[0].message["content"]

    # Llamadas a GPT-4 para generar el análisis en inglés
    response_en = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt_en}]
    )
    mensaje_en = response_en.choices[0].message["content"]

    # URL base para enviar mensajes via bot de Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    # Enviar el mensaje en español
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

    # Enviar el mensaje en inglés
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
