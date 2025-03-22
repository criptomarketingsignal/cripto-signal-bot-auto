from datetime import datetime

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

fecha = obtener_fecha_en_espanol()

prompt = f"""
Actúa como un analista técnico profesional especializado en criptomonedas y genera un mensaje REALISTA para hoy con datos actualizados, ideal para enviar por Telegram.

➡️ Tu objetivo es entregar una señal operable en long 3x para Bitcoin (BTCUSD) con datos precisos y actuales. La estructura del mensaje debe ser la siguiente:

Buenos días traders! Que mejor manera de comenzar el día que con nuestra primera señal del día. Hoy vamos a analizar Bitcoin y darles nuestras recomendaciones. ¡Vamos allá!

𝐀𝓢𝓱𝓲: {fecha}  
𝓎𝓮𝓰𝓳: 1 de 3

Nuestro equipo trabaja arduamente para ofrecer análisis técnico y fundamental en tiempo real tres veces al día, asegurándonos de mantener a nuestra comunidad completamente informada y preparada.

En nuestro análisis técnico, utilizamos las herramientas más confiables, como:
- Velas japonesas 📊
- Medias Móviles Exp 📈
- Fibonacci 🔢
- Fuerza Relativa (RSI) ⚖️
- (SQZMOM) ⚡️
- Volumen (POC) 💼

◉ 𝐀𝓢𝓷𝓶𝓳𝓸𝓮 𝓣𝓢𝓮𝓲𝓳:
Escribe aquí un resumen claro y actual del análisis técnico de BTC usando los indicadores mencionados y coloca valores reales. Incluye:
📊 Velas: ...  
📈 EMAs: ...  
🔁 Fibonacci: ...  
🧱 POC: ...  
⚡️ RSI: ...  
🚀 SQZMOM: ...

◉ 𝐀𝓢𝓷𝓶𝓲𝓶𝓳𝓲𝓸𝓰 𝓦𝓲𝓵𝓲𝓶𝓳:
💵 DXY: ...  
🧠 Sentimiento: ...  
📈 Nasdaq/SP500: ...

◉ 𝐑𝓦𝓮𝓲 𝓵𝓸 𝓸𝓶𝓳𝓸𝓲𝓰𝓸 (𝐋𝐨𝐧𝐠 𝟑𝐱):
Escribe un rango real y actual, con precios válidos y realistas, basados en análisis técnico del mercado de hoy:

💰 Entrada óptima entre: [precio más bajo] y [precio más alto]  
🎯 Rango de operación: [mismo rango]  
🟢 Probabilidad de éxito estimada: [porcentaje técnico justificado]  

⚠️ ¡Cuida tu gestión de riesgo! No te olvides de establecer una estrategia de salida. Este mercado es altamente volátil, operación recomendada solo para hoy.

📊 Señales, gráficos en vivo y análisis en tiempo real completamente GRATIS por 30 días. 

🔑 𝐋𝓇𝓦𝓢𝓡 𝓴𝓲 𝓸𝓻 𝓸𝓲 𝓵𝓲𝓳𝓸! 🚀
Gracias por elegirnos como tu portal de trading de confianza. ¡Juntos, haremos que tu inversión crezca!

✨ 𝐇𝓲𝓪𝓵𝓲 𝓸𝓲𝓮𝓳 𝐁𝓪 ✨ Mantente pendiente del segundo mensaje (mitad de sesión, hora de Nueva York). ¡Feliz trading!
"""
