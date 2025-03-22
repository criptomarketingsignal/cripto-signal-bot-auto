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

    prompt_es = f"""
Actúa como un analista técnico profesional especializado en criptomonedas y genera un mensaje en español perfectamente estructurado para el canal de señales de Telegram.

✅ Este es un análisis real de Bitcoin (BTCUSD) en timeframe intradía, para operaciones en LONG con apalancamiento 3x.  
✅ El análisis debe incluir SIEMPRE un rango de entrada real y actualizado, con al menos 2% de amplitud entre mínimo y máximo (por ejemplo: $83,200 – $84,900).  
✅ Usa análisis técnico multitemporal (1W, 1D, 4H, 1H) con RSI, EMAs, Fibonacci, SQZMOM, POC y velas japonesas.  
✅ Usa también análisis fundamental con DXY, sentimiento de mercado y Nasdaq/SP500.  
✅ Escribe el mensaje para Telegram, con viñetas ◉, emoticonos, y negritas estilo unicode (𝐞𝐬𝐭𝐞 𝐭𝐢𝐩𝐨). Nunca uses Markdown.  
✅ No uses frases genéricas como "el rango más favorable". Siempre da precios reales, actuales y confiables.

Formato del mensaje:

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
Describe RSI, EMAs, Fibonacci, volumen, SQZMOM y patrones de velas.

◉ 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥:  
DXY, sentimiento del mercado, SP500/Nasdaq.

◉ 𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧 (𝐋𝐨𝐧𝐠 𝟑𝐱):  
💰 Entrada óptima: Indica precios reales en formato $xx,xxx – $xx,xxx  
🟢 Probabilidad de éxito: Debe calcularse con base en indicadores  
⚠️ Gestión de riesgo obligatoria. Rango válido solo para hoy.

📊 Señales, gráficos en vivo y análisis en tiempo real completamente GRATIS por 30 días.  
🔑 𝐎𝐛𝐭𝐞́𝐧 𝐭𝐮 𝐦𝐞𝐬 𝐠𝐫𝐚𝐭𝐢𝐬 𝐚𝐡𝐨𝐫𝐚! 🚀

Muchas gracias por confiar en nosotros como tu portal de trading. Juntos haremos crecer tu inversión.  
✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨ Estén atentos para el 2º mensaje (mitad de sesión, Hora de Nueva York). ¡Feliz trading!
"""

    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[{"role": "user", "content": prompt_es}]
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
