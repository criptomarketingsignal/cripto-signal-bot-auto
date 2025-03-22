import os
import requests
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_CHAT_ID_ES = "-1002440626725"

def send_prompt_01():
    fecha_hoy = datetime.now().strftime("%d de %B de %Y")

    prompt = (
        f"Actúa como un analista técnico profesional especializado en criptomonedas y realiza un análisis detallado del precio de Bitcoin "
        f"para hoy, {fecha_hoy}. Tu mensaje debe tener un tono claro, motivador y convincente, usando formato de Telegram (sin Markdown).\n"
        f"\n"
        f"Empieza el mensaje con un texto motivador que diga que esta es la primera señal del día.\n"
        f"Luego presenta un análisis con este formato:\n"
        f"\n"
        f"𝐅𝐞𝐜𝐡𝐚: {fecha_hoy}\n"
        f"\n"
        f"◉ 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐓𝐞́𝐜𝐧𝐢𝐜𝐨:\n"
        f"📊 Velas: ...\n"
        f"📈 EMAs: ...\n"
        f"🔁 Fibonacci: ...\n"
        f"🧱 POC: ...\n"
        f"⚡ RSI: ...\n"
        f"🚀 SQZMOM: ...\n"
        f"\n"
        f"◉ 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥:\n"
        f"💵 DXY: ...\n"
        f"🧠 Sentimiento: ...\n"
        f"📈 Nasdaq/SP500: ...\n"
        f"\n"
        f"◉ 𝐒𝐞𝐧̃𝐚𝐥 𝐝𝐞 𝐓𝐫𝐚𝐝𝐢𝐧𝐠 (𝐋𝐨𝐧𝐠 𝟑𝐱):\n"
        f"💰 Entrada:\n"
        f"🎯 Take Profit:\n"
        f"🛑 Stop Loss:\n"
        f"\n"
        f"⚠️ ¡Cuida tu gestión de riesgo!\n"
        f"\n"
        f"Crypto Signal Bot analiza por ti... pendiente del mensaje de mitad de sesión."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    message = response.choices[0].message["content"]

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_CHAT_ID_ES,
        "text": message,
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

    requests.post(url, json=payload)
