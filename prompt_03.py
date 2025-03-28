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
    rango_min = round(precio * 0.9925, 2)   # -0.75%
    rango_max = round(precio * 1.0025, 2)   # +0.25%
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
    Actúa como un analista técnico profesional especializado en criptomonedas. Tu tarea es generar un análisis estructurado, preciso y orientado a resultados del comportamiento de Bitcoin (BTCUSD) al cierre de la vela diaria. Enfócate exclusivamente en oportunidades LONG de corto plazo.

📊 El análisis debe estar basado en el gráfico de 1 hora, pero considerar multitemporalidad (4H y 1D) para mayor contexto. El precio actual de BTC es {precio_btc} USD.

✅ Instrucciones:

1. Analiza cómo se desarrolló el comportamiento de BTC durante el día actual. 
2. Evalúa si hubo un movimiento fuerte, una caída importante o consolidación, y si se respetaron los niveles claves del análisis anterior.
3. Determina si hubo algún evento macroeconómico o político relevante (por ejemplo: decisión de tasas de la FED, informe CPI, datos de empleo, conflictos globales, declaraciones de Trump o Biden, etc.), y cómo impactó el precio.
4. Proyecta el posible comportamiento para el día siguiente, basado en patrones actuales, volumen y estructura del mercado. 
5. Sugiere si mañana podría haber una entrada LONG favorable o si es mejor esperar confirmación.

📌 Herramientas a considerar (menciónalas si aportan valor al análisis):
- Velas japonesas
- EMAs 21, 55, 100, 200
- RSI
- SQZMOM
- Volumen (POC)
- Retrocesos de Fibonacci en 1D y 4H (para tu análisis interno, no los menciones directamente)

🎯 El mensaje debe ser claro, directo, motivador, en español neutro y con una estructura profesional. No uses frases genéricas. Justifica siempre tus observaciones con datos reales del día.

Usa esta estructura exacta en el mensaje generado:

✨ Qué mejor momento que el cierre de la vela diaria para evaluar el panorama completo. ¡Vamos a analizar Bitcoin con todo!

𝐅𝐞𝐜𝐡𝐚: {fecha_hoy}  
𝐒𝐞𝐧̃𝐚𝐥: 3 de 3

Nuestro equipo trabaja arduamente para ofrecer análisis técnico y fundamental en tiempo real tres veces al día, asegurándonos de mantener a nuestra comunidad completamente informada y preparada.

---
agrega un texto breve resumen general de esto:
🧠 → 𝐑𝐞𝐬𝐮𝐦𝐞𝐧 𝐆𝐞𝐧𝐞𝐫𝐚𝐥:

1. Analiza cómo se desarrolló el comportamiento de BTC durante el día actual. 
2. Evalúa si hubo un movimiento fuerte, una caída importante o consolidación, y si se respetaron los niveles claves del análisis anterior.
3. Determina si hubo algún evento macroeconómico o político relevante (por ejemplo: decisión de tasas de la FED, informe CPI, datos de empleo, conflictos globales, declaraciones de Trump o Biden, etc.), y cómo impactó el precio.
4. Proyecta el posible comportamiento para el día siguiente, basado en patrones actuales, volumen y estructura del mercado. 
5. Sugiere si mañana podría haber una entrada LONG favorable o si es mejor esperar confirmación.

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

📊 Señales, gráficos en vivo y análisis en tiempo real completamente GRATIS por 30 días.  
🔑 𝐎𝐛𝐭𝐞́𝐧 𝐭𝐮 𝐦𝐞𝐬 𝐠𝐫𝐚𝐭𝐢𝐬 𝐚𝐡𝐨𝐫𝐚! 🚀  

Gracias por elegirnos como tu portal de trading de confianza. ¡Juntos, haremos que tu inversión crezca!  
✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨ Te esperamos mañana para nuevas oportunidades. ¡Feliz trading!
"""

    prompt_en = f"""
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

What better time than mid-session to reassess opportunities. Let’s dive into Bitcoin!

𝐃𝐚𝐭𝐞: {fecha_hoy}  
𝐒𝐢𝐠𝐧𝐚𝐥: 3 of 3

Our team works hard to deliver real-time technical and fundamental analysis three times a day, ensuring our community is fully informed and ready to act.

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
⚠️ Always manage risk. Set your exit strategy. Crypto is highly volatile.//

---
📊 Live signals, real-time charts, and in-depth analysis — absolutely FREE for 30 days.  
🔑 𝐂𝐥𝐚𝐢𝐦 𝐲𝐨𝐮𝐫 𝐅𝐑𝐄𝐄 𝐦𝐨𝐧𝐭𝐡 𝐭𝐨𝐝𝐚𝐲! 🚀  

Thank you for choosing us as your trusted trading partner. Together, we’ll make your investment grow!  
✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨ See you tomorrow for more opportunities. Happy trading!
"""

    response_es = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt_es}]
    )
    message_es = response_es.choices[0].message["content"]

    response_en = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt_en}]
    )
    message_en = response_en.choices[0].message["content"]

    url_text = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    url_img = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    # Enviar imagen a ambos canales
    for chat_id in [CHANNEL_CHAT_ID_ES, CHANNEL_CHAT_ID_EN]:
        requests.post(url_img, data={
            "chat_id": chat_id,
            "photo": "https://cryptosignalbot.com/wp-content/uploads/2025/03/fin-ses.png"
        })

    payload_es = {
        "chat_id": CHANNEL_CHAT_ID_ES,
        "text": message_es,
        "parse_mode": "HTML",
        "reply_markup": {
            "inline_keyboard": [[
                {
                    "text": "🎯 Señales premium 30 días gratis",
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
                    "text": "🎯 Free Premium Signals 30 Days",
                    "url": "https://t.me/CriptoSignalBotGestion_bot?start=676731307b8344cb070ac996"
                }
            ]]
        }
    }

    requests.post(url_text, json=payload_es)
    requests.post(url_text, json=payload_en)
