import os
import requests
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_CHAT_ID_ES = "-1002440626725"
CHANNEL_CHAT_ID_EN = "-1002288256984"

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

def obtener_fecha_es():
    meses = {
        "January": "enero", "February": "febrero", "March": "marzo",
        "April": "abril", "May": "mayo", "June": "junio",
        "July": "julio", "August": "agosto", "September": "septiembre",
        "October": "octubre", "November": "noviembre", "December": "diciembre"
    }
    ahora = datetime.now()
    mes_es = meses[ahora.strftime("%B")]
    return f"{ahora.day} de {mes_es} de {ahora.year}"

def send_prompt_01():
    fecha_hoy = obtener_fecha_es()
    precio_btc = obtener_precio_btc()
    if not precio_btc:
        return

    rango_min, rango_max, promedio, efectividad = calcular_rango_y_efectividad(precio_btc)

    prompt_es = f"""
🚫 𝐏𝐑𝐎𝐇𝐈𝐁𝐈𝐃𝐎 𝐀𝐁𝐒𝐎𝐋𝐔𝐓𝐀𝐌𝐄𝐍𝐓𝐄 usar negrillas tradicionales.  
❌ Nunca, jamás utilices doble asterisco (**) para resaltar palabras.  
❌ No uses ningún tipo de formato de negrita convencional.  
🔒 Está terminantemente prohibido insertar asteriscos en el texto.  
✅ Si deseas destacar algo, usa únicamente letras decorativas tipo unicode (por ejemplo: 𝐒𝐞𝐧̃𝐚𝐥, 𝐀𝐜𝐭𝐢𝐯𝐨, 𝐑𝐞𝐬𝐮𝐥𝐭𝐚𝐝𝐨).  
𝐍𝐮𝐧𝐜𝐚 𝐮𝐬𝐞𝐬 𝐚𝐬𝐭𝐞𝐫𝐢𝐬𝐜𝐨𝐬. 𝐍𝐮𝐧𝐜𝐚 𝐮𝐬𝐞𝐬 𝐧𝐞𝐠𝐫𝐢𝐭𝐚𝐬 𝐜𝐨𝐦𝐮𝐧𝐞𝐬. 𝐍𝐮𝐧𝐜𝐚.

📊 El análisis debe estar basado en el gráfico de 1 hora, pero considerar multitemporalidad (4H y 1D) para mayor contexto. El precio actual de BTC es {precio_btc} USD.

✅ 𝐈𝐧𝐬𝐭𝐫𝐮𝐜𝐜𝐢𝐨𝐧𝐞𝐬:

1. Analiza el comportamiento de BTC desde el cierre de la vela diaria anterior hasta el momento actual.  
2. Evalúa si hubo un movimiento fuerte, una caída importante o consolidación.  
3. Proyecta el posible comportamiento para el día actual, basado en patrones actuales, volumen y estructura del mercado.  
4. Sugiere si hoy podría haber una entrada LONG favorable o si es mejor esperar confirmación.  

📅 → 𝐄𝐯𝐞𝐧𝐭𝐨𝐬 𝐌𝐚𝐜𝐫𝐨𝐞𝐜𝐨𝐧𝐨́𝐦𝐢𝐜𝐨𝐬 𝐝𝐞 𝐄𝐄.𝐔𝐔. 𝐜𝐨𝐧 𝐢𝐦𝐩𝐚𝐜𝐭𝐨 𝐚𝐥𝐭𝐨 (𝐬𝐢 𝐡𝐚𝐲):

Revisa el calendario económico del día de hoy y responde lo siguiente solo si hay eventos de alto impacto:

- 🕒 ¿A qué hora se publican? (hora de Nueva York)  
- 📰 ¿Qué tipo de evento es? (ej. decisión de tasas, NFP, CPI...)  
- 💥 ¿Qué impacto puede tener? (¿favorable o desfavorable para el dólar?)  
- 🔄 ¿Cómo se relaciona esto con BTC? Recuerda: si es favorable para el dólar, es negativo para la bolsa y para Bitcoin.  
- 📊 ¿Cuál es la probabilidad de que afecte el precio de BTC hoy?

Concluye con una frase clara:  
👉 ¿Estos eventos aumentan la volatilidad? ¿Conviene operar con precaución hoy?

✨ Buenos días traders! Qué mejor manera de comenzar el día que con nuestra primera señal del día. Hoy vamos a analizar Bitcoin y darles nuestras recomendaciones. ¡Vamos allá!

🕘 𝐅𝐞𝐜𝐡𝐚: {fecha_hoy}  
🌞 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐈𝐧𝐢𝐜𝐢𝐚𝐥 – 𝐒𝐞𝐧̃𝐚𝐥 𝟏 𝐝𝐞 𝟑  
𝐍𝐮𝐞𝐬𝐭𝐫𝐨 𝐞𝐪𝐮𝐢𝐩𝐨 𝐭𝐫𝐚𝐛𝐚𝐣𝐚 𝐚𝐫𝐝𝐮𝐚𝐦𝐞𝐧𝐭𝐞 𝐩𝐚𝐫𝐚 𝐨𝐟𝐫𝐞𝐜𝐞𝐫 𝐚𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐞𝐧 𝐭𝐢𝐞𝐦𝐩𝐨 𝐫𝐞𝐚𝐥 𝐭𝐫𝐞𝐬 𝐯𝐞𝐜𝐞𝐬 𝐚 𝐥𝐝𝐢́𝐚.

🧠 → 𝐑𝐞𝐬𝐮𝐦𝐞𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐥  
1. Comportamiento de BTC desde el inicio del día.  
2. ¿Movimiento fuerte, caída o consolidación?  
3. ¿Se respetaron niveles del análisis anterior?  
4. ¿Hubo eventos macroeconómicos o políticos influyentes?  
5. Proyección para mañana y si es recomendable una entrada long o esperar.

📊 → 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐓𝐞́𝐜𝐧𝐢𝐜𝐨

𝟏. 𝐆𝐫𝐚́𝐟𝐢𝐜𝐨 𝐃𝐢𝐚𝐫𝐢𝐨  
• Tendencia general actual  

𝟐. 𝐆𝐫𝐚́𝐟𝐢𝐜𝐨 𝐝𝐞 𝟒𝐇  
• Velas y dirección dominante  
• Zonas clave de rebote o congestión  
• RSI y volumen brevemente

𝟑. 𝐆𝐫𝐚́𝐟𝐢𝐜𝐨 𝐝𝐞 𝟏𝐇  
• Patrones de velas y estructuras  
• Soportes/resistencias  
• EMAs dinámicas  
• RSI (sobrecompra/sobreventa o divergencias)  
• Volumen (POC y zonas clave)  
• SQZMOM: compresión, expansión y momentum  

🔍 → 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥  
Evalúa si hay eventos macroeconómicos, políticos o geopolíticos con potencial de mover BTC hoy. Considera:

• Reuniones de la FED, informes CPI, NFP, etc.  
• Índice del dólar (DXY)  
• Declaraciones de figuras como Trump o Biden  
• Narrativa del mercado, sentimiento general  
• Relación con el SP500 o Nasdaq si aplica

⚠️ Si hay alta incertidumbre, indica que hoy 𝐧𝐨 𝐞𝐬 𝐫𝐞𝐜𝐨𝐦𝐞𝐧𝐝𝐚𝐛𝐥𝐞 𝐨𝐩𝐞𝐫𝐚𝐫 y que es mejor esperar confirmaciones más claras.

🚨 → 𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐎𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧 (𝐋𝐨𝐧𝐠 𝟑𝐱)

💰 𝐏𝐫𝐞𝐜𝐢𝐨 𝐝𝐞 𝐄𝐧𝐭𝐫𝐚𝐝𝐚 𝐎́𝐩𝐭𝐢𝐦𝐨: nivel ajustado técnico  
🎯 𝐑𝐚𝐧𝐠𝐨 𝐃𝐢𝐚𝐫𝐢𝐨: ~2% operable en gráfico 1H  
🟢 𝐏𝐫𝐨𝐛𝐚𝐛𝐢𝐥𝐢𝐝𝐚𝐝 𝐝𝐞 𝐄𝐱𝐢𝐭𝐨: resultado técnico + fundamental

Si es >70%:

🔁 𝐎𝐩𝐨𝐫𝐭𝐮𝐧𝐢𝐝𝐚𝐝 𝐝𝐞 𝐀𝐥𝐭𝐚 𝐏𝐫𝐞𝐜𝐢𝐬𝐢𝐨́𝐧  
𝐄𝐬𝐭𝐫𝐚𝐭𝐞𝐠𝐢𝐚: abrir y cerrar posiciones dentro del rango diario.

Si es <70%:

⚠️ 𝐍𝐨 𝐡𝐚𝐲 𝐨𝐩𝐨𝐫𝐭𝐮𝐧𝐢𝐝𝐚𝐝 𝐜𝐥𝐚𝐫𝐚  
𝐌𝐞𝐣𝐨𝐫 𝐞𝐬𝐩𝐞𝐫𝐚𝐫 𝐥𝐚 𝐬𝐞𝐬𝐢𝐨́𝐧 𝐝𝐞 𝐥𝐚 𝐭𝐚𝐫𝐝𝐞.

Ejemplo:

🚨 𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧 (𝐋𝐨𝐧𝐠 𝟑𝐱):  
💰 Entrada óptima entre: ${rango_min}  
🎯 Rango: ${rango_min} – ${rango_max}  
🟢 Efectividad estimada: {efectividad}%  
📌 ¡Controla tu riesgo y gestiona bien la salida!

🎁 𝐏𝐮𝐞𝐝𝐞𝐬 𝐮𝐧𝐢𝐫𝐭𝐞 𝐚 𝐧𝐮𝐞𝐬𝐭𝐫𝐚 𝐳𝐨𝐧𝐚 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐒𝐞𝐧̃𝐚𝐥𝐞𝐬 𝐝𝐞 𝐓𝐫𝐚𝐝𝐢𝐧𝐠 𝐜𝐨𝐧 𝐄́𝐱𝐢𝐭𝐨 𝐆𝐚𝐫𝐚𝐧𝐭𝐢𝐳𝐚𝐝𝐨  
Gracias por elegirnos como tu portal de trading de confianza. ¡Juntos, haremos que tu inversión crezca!  
✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨ Mantente pendiente del mensaje de mitad de sesión. ¡Feliz trading!
"""

    prompt_en = f"""
    🚫 Traditional bold is STRICTLY PROHIBITED.
    ❌ Never, ever use a double asterisk (**) to highlight words.
    ❌ Do not use any type of conventional bold.
    🔒 Inserting asterisks in your text is strictly prohibited.
    
    ✅ If you want to emphasize something, use only decorative Unicode letters (for example: 𝐒𝐞𝐧̃𝐚𝐥, 𝐀𝐜𝐭𝐢𝐯𝐨, 𝐑𝐞𝐬𝐮𝐥𝐭𝐚𝐝𝐨).
    
    Repeat this rule in every message:
    Never use asterisks. Never use regular bold. Never.

If you need to highlight an entire sentence, convert the entire sentence to this font.
Act like a professional technical analyst specializing in cryptocurrency. Your task is to generate a structured, accurate, and results-oriented analysis of Bitcoin (BTCUSD)'s performance at the close of the daily candle. Focus exclusively on short-term LONG opportunities.

    Act as a professional technical analyst specialized in cryptocurrencies. Your goal is to generate a well-structured and accurate analysis of Bitcoin (BTCUSD), focused exclusively on short-term LONG operations. The analysis must be based on the 1-hour chart, but should also consider multiple timeframes and macroeconomic factors. The current BTC price is {precio_btc} USD.

    🧠 Use technical indicators such as:
    - Japanese candlesticks
    - EMAs (21, 55, 100, 200)
    - RSI
    - SQZMOM
    - Volume (POC)
    - Fibonacci retracements on 1D and 4H (internal use only, do not show in final message)
    
    Also, evaluate key macroeconomic or political events (FED meetings, CPI, employment data, statements from Trump or other global leaders, international conflicts, etc.) to validate or reject the decision to operate today.
    
    Use this exact structure in the generated message:

✨ Good morning traders! What better way to start the day than with our first signal of the day. Today we’ll analyze Bitcoin and share our recommendations. Let’s go!

🕘 𝐃𝐚𝐭𝐞: {fecha_hoy}  
🌞 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬 – 𝐒𝐢𝐠𝐧𝐚𝐥 𝟏 𝐨𝐟 𝟑 

Our team works hard to provide real-time technical and fundamental analysis three times a day, ensuring our community is fully informed and prepared.

---
Add a brief general summary of this:
🧠 → 𝐆𝐞𝐧𝐞𝐫𝐚𝐥 𝐑𝐞𝐬𝐮𝐦𝐞𝐧:
1. Analyze how BTC's behavior developed during the current day.
2. Evaluate whether there was a strong movement, a significant drop, or consolidation, and whether the key levels from the previous analysis were respected.
3. Determine if there were any relevant macroeconomic or political events (e.g., Fed rate decision, CPI report, employment data, global conflicts, statements by Trump or Biden, etc.), and how they impacted the price.
4. Project possible behavior for the next day, based on current patterns, volume, and market structure.
5. Suggest whether there could be a favorable LONG entry tomorrow or if it is better to wait for confirmation.

---
📊 → 𝐓𝐞𝐜𝐡𝐧𝐢𝐜𝐚𝐥 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬:
𝟏. 𝐃𝐚𝐢𝐥𝐲 𝐂𝐡𝐚𝐫𝐭 (𝟏𝐃)  
Brief summary including:  
- Overall daily trend

𝟐. 𝟒-𝐇𝐨𝐮𝐫 𝐂𝐡𝐚𝐫𝐭 (𝟒𝐇)  
Brief summary including:  
- Candle structure and dominant direction  
- Key bounce or congestion zones  
- Quick read of RSI and volume

𝟑. 𝟏-𝐇𝐨𝐮𝐫 𝐂𝐡𝐚𝐫𝐭 (𝟏𝐇)  
- Candle patterns (engulfing, doji, hammer, etc.)  
- Precise support and resistance  
- EMAs (21, 55, 100, 200) as dynamic S/R  
- Fibonacci retracements (38.2%, 50%, 61.8%, 78.6%)  
- RSI with commentary on overbought/oversold and divergences  
- Volume with Point of Control and accumulation/distribution zones  
- SQZMOM direction and compression/expansion analysis

---
🔍 → 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬
Evaluate any important macroeconomic, political, or geopolitical events that could impact BTC today, including:

- Key events like FED meetings, CPI, NFP releases, etc.  
- Movement of the US Dollar Index (DXY)  
- News from political figures like Donald Trump, regulatory announcements, or global tensions  
- General market sentiment (whales, social narratives, risk appetite)  
- Correlation with indices like SP500 or Nasdaq if relevant

⚠️ If there are **high-impact news or political statements creating significant uncertainty**, make it clear that **it’s not a favorable time to trade**, or that probabilities are low. Suggest waiting for confirmations.

This information must be analyzed and used to **calculate the final probability of success**, but does not need to be fully listed unless highly relevant.

---
🚨 𝐎𝐩𝐞𝐫𝐚𝐛𝐥𝐞 𝐑𝐚𝐧𝐠𝐞 (𝐋𝐨𝐧𝐠 𝟑𝐱):

Based on the full technical and fundamental analysis, calculate:

- 💰 𝐎𝐩𝐭𝐢𝐦𝐮𝐦 𝐄𝐧𝐭𝐫𝐲 𝐏𝐫𝐢𝐜𝐞: as technically precise as possible  
- 🎯 𝐎𝐩𝐞𝐫𝐚𝐛𝐥𝐞 𝐑𝐚𝐧𝐠𝐞: maximum 2%, based on the 1-hour chart  
- 🟢 𝐄𝐬𝐭𝐢𝐦𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬 𝐏𝐫𝐨𝐛𝐚𝐛𝐢𝐥𝐢𝐭𝐲: result (%) from combined technical + fundamental analysis

If the probability is higher than 70%, indicate:

🔁 𝐇𝐢𝐠𝐡-𝐏𝐫𝐞𝐜𝐢𝐬𝐢𝐨𝐧 𝐎𝐩𝐩𝐨𝐫𝐭𝐮𝐧𝐢𝐭𝐲  
𝐓𝐡𝐞 𝐛𝐞𝐬𝐭 𝐬𝐭𝐫𝐚𝐭𝐞𝐠𝐲 𝐢𝐬 𝐭𝐨 𝐨𝐩𝐞𝐧 𝐚𝐧𝐝 𝐜𝐥𝐨𝐬𝐞 𝐬𝐡𝐨𝐫𝐭 𝐢𝐧𝐭𝐫𝐚𝐝𝐚𝐲 𝐭𝐫𝐚𝐝𝐞𝐬 𝐰𝐢𝐭𝐡𝐢𝐧 𝐭𝐡𝐞 𝐫𝐚𝐧𝐠𝐞.  
𝐓𝐚𝐤𝐞 𝐚𝐝𝐯𝐚𝐧𝐭𝐚𝐠𝐞 𝐨𝐟 𝐦𝐨𝐦𝐞𝐧𝐭𝐮𝐦 𝐚𝐧𝐝 𝐜𝐨𝐧𝐬𝐨𝐥𝐢𝐝𝐚𝐭𝐢𝐨𝐧.

If probability is below 70%, indicate:

⚠️ 𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐧𝐨 𝐜𝐥𝐞𝐚𝐫 𝐨𝐩𝐞𝐫𝐚𝐭𝐢𝐨𝐧𝐚𝐥 𝐬𝐞𝐭𝐮𝐩 𝐢𝐬 𝐝𝐞𝐭𝐞𝐜𝐭𝐞𝐝.  
𝐌𝐚𝐫𝐤𝐞𝐭 𝐜𝐨𝐧𝐝𝐢𝐭𝐢𝐨𝐧𝐬 𝐚𝐫𝐞 𝐧𝐨𝐭 𝐟𝐚𝐯𝐨𝐫𝐚𝐛𝐥𝐞 𝐚𝐧𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬 𝐩𝐫𝐨𝐛𝐚𝐛𝐢𝐥𝐢𝐭𝐲 𝐢𝐬 𝐥𝐨𝐰.  
📌 𝐖𝐚𝐢𝐭 𝐟𝐨𝐫 𝐭𝐡𝐞 𝐦𝐢𝐝-𝐬𝐞𝐬𝐬𝐢𝐨𝐧 𝐚𝐧𝐚𝐥𝐲𝐬𝐢𝐬 𝐭𝐨 𝐠𝐞𝐭 𝐛𝐞𝐭𝐭𝐞𝐫 𝐜𝐨𝐧𝐟𝐢𝐫𝐦𝐚𝐭𝐢𝐨𝐧𝐬.

Example output format:

🚨 𝐎𝐩𝐞𝐫𝐚𝐛𝐥𝐞 𝐑𝐚𝐧𝐠𝐞 (𝐋𝐨𝐧𝐠 𝟑𝐱):

💰 Optimum entry price: ${rango_min}  
🎯 Operable range: Between ${rango_min} – ${rango_max}  
🟢 Estimated success rate: {efectividad}%  
Ideal for short intraday trades within this range.  
⚠️ Always manage risk. Set your exit strategy. Crypto is highly volatile.

---
🎁 𝐘𝐨𝐮 𝐜𝐚𝐧 𝐣𝐨𝐢𝐧 𝐨𝐮𝐫 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐙𝐨𝐧𝐞 — 𝐓𝐫𝐚𝐝𝐢𝐧𝐠 𝐒𝐢𝐠𝐧𝐚𝐥𝐬 𝐰𝐢𝐭𝐡 𝐆𝐮𝐚𝐫𝐚𝐧𝐭𝐞𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬 

Thank you for choosing us as your trusted trading partner. Together, we’ll make your investment grow!  
✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨ Stay tuned for the mid-session update. Happy trading!
"""

    response_es = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt_es}]
    )
    message_es = response_es.choices[0].message["content"]

    response_en = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt_en}]
    )
    message_en = response_en.choices[0].message["content"]

    url_text = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    url_img = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    # Enviar imagen a ambos canales
    for chat_id in [CHANNEL_CHAT_ID_ES, CHANNEL_CHAT_ID_EN]:
        requests.post(url_img, data={
            "chat_id": chat_id,
            "photo": "https://cryptosignalbot.com/wp-content/uploads/2025/03/principio.png"
        })

    payload_es = {
        "chat_id": CHANNEL_CHAT_ID_ES,
        "text": message_es,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [[
                {
                    "text": "🎯 Señales premium",
                    "url": "https://t.me/CriptoSignalBotGestion_bot?start=676731307b8344cb070ac996"
                }
            ]]
        }
    }

    payload_en = {
        "chat_id": CHANNEL_CHAT_ID_EN,
        "text": message_en,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [[
                {
                    "text": "🎯 Premium Signals",
                    "url": "https://t.me/CriptoSignalBotGestion_bot?start=676731307b8344cb070ac996"
                }
            ]]
        }
    }

    requests.post(url_text, json=payload_es)
    requests.post(url_text, json=payload_en)
