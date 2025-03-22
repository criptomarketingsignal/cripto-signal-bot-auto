import os
import requests
import openai
from datetime import datetime
import json

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_CHAT_ID_ES = "-1002440626725"
CHANNEL_CHAT_ID_EN = "-1002288256984"

# Ruta para guardar el análisis completo
FULL_ANALYSIS_PATH = "btc_full_analysis_es.txt"

def send_prompt_01():
    fecha_hoy = datetime.now().strftime("%d de %B de %Y")

    # Prompt para mensaje corto
    prompt_resumen_es = (
        f"Genera una señal operable en long para Bitcoin con apalancamiento 3x para hoy, {fecha_hoy}. "
        "Incluye: rango de compra, promedio de entrada, take profit, stop loss, resumen técnico, resumen fundamental. "
        "Escríbelo con estilo motivador y claro, usando negritas en unicode (𝐞𝐬𝐭𝐞 𝐭𝐢𝐩𝐨), viñetas ◉, y emoticonos. "
        "Al final, agrega: 'Crypto Signal Bot analiza por ti... pendiente del mensaje de mitad de sesión'."
    )

    # Prompt para mensaje largo
    prompt_detallado_es = (
        f"Realiza un análisis técnico y fundamental completo y detallado del precio de Bitcoin (BTCUSD) para hoy, {fecha_hoy}, "
        "siguiendo este formato: multitemporalidades (1W, 1D, 4H, 1H), velas japonesas, niveles de soporte/resistencia, "
        "EMAs 21/55/100/200, retrocesos de Fibonacci (38.2%, 50%, 61.8%), volumen (POC), RSI, SQZMOM, eventos fundamentales, "
        "movimiento del DXY, sentimiento del mercado y relación con SP500/Nasdaq. "
        "Finaliza indicando si es buen día para operar en long o no, y da el entry ideal. Formatea el texto como si fuera un informe técnico para Telegram."
    )

    # Obtener mensaje corto
    response_corto = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt_resumen_es}]
    )
    mensaje_corto = response_corto.choices[0].message["content"]

    # Obtener mensaje largo
    response_largo = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt_detallado_es}]
    )
    mensaje_largo = response_largo.choices[0].message["content"]

    # Guardar análisis completo
    with open(FULL_ANALYSIS_PATH, "w", encoding="utf-8") as f:
        f.write(mensaje_largo)

    # Enviar mensaje corto con botones a Telegram
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_CHAT_ID_ES,
        "text": mensaje_corto,
        "parse_mode": "HTML",
        "reply_markup": json.dumps({
            "inline_keyboard": [
                [
                    {
                        "text": "✨ Señales premium 30 días gratis",
                        "url": "https://t.me/CriptoSignalBotGestion_bot?start=676731307b8344cb070ac996"
                    }
                ],
                [
                    {
                        "text": "🔎 Solicitar análisis completo y detallado",
                        "url": "https://t.me/CriptoSignalBotGestion_bot?start=btccompleto"
                    }
                ]
            ]
        })
    }

    requests.post(url, data=payload)

