import os
import requests
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_CHAT_ID_ES = "-1002440626725"

def enviar_senal_con_imagen_y_texto_largo():
    # 1) Texto corto para el caption de la foto
    caption_corto = (
        "📊 Buenos días traders! \n"
        "Hoy analizamos Bitcoin y te traemos nuestra señal.\n"
        "¡Mira el siguiente mensaje para ver el análisis detallado!"
    )

    # 2) Análisis extenso que excede el límite del caption
    mensaje_largo = (
        "Aquí va tu análisis extenso y detallado, que puede superar los 1024 "
        "caracteres sin problema, incluyendo herramientas, soportes, resistencias, "
        "Fibonacci, etc. \n\n"
        "Recuerda que este texto se envía con sendMessage, donde Telegram permite hasta "
        "4096 caracteres. Así evitas el límite del caption en sendPhoto. \n\n"
        "También aquí puedes incluir tu botón con inline_keyboard si deseas."
    )

    # 3) Enviar la imagen + caption corto
    url_sendPhoto = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    imagen_url = "https://cryptosignalbot.com/wp-content/uploads/2025/03/ini.png"
    
    # Inline keyboard para la foto (opcional)
    keyboard_foto = {
        "inline_keyboard": [[
            {
                "text": "Señales premium 30 días gratis ✨",
                "url": "https://t.me/CriptoSignalBotGestion_bot?start=xxxx"
            }
        ]]
    }

    requests.post(
        url_sendPhoto,
        json={
            "chat_id": CHANNEL_CHAT_ID_ES,
            "photo": imagen_url,
            "caption": caption_corto,
            "parse_mode": "HTML",
            "reply_markup": keyboard_foto
        }
    )

    # 4) Enviar el mensaje largo (texto)
    url_sendMessage = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    # Inline keyboard para el mensaje largo (opcional, puede ser diferente)
    keyboard_mensaje = {
        "inline_keyboard": [[
            {
                "text": "Más info",
                "url": "https://t.me/CriptoSignalBotGestion_bot?start=xxxx"
            }
        ]]
    }

    requests.post(
        url_sendMessage,
        json={
            "chat_id": CHANNEL_CHAT_ID_ES,
            "text": mensaje_largo,
            "parse_mode": "HTML",
            "reply_markup": keyboard_mensaje
        }
    )

if __name__ == "__main__":
    enviar_senal_con_imagen_y_texto_largo()

