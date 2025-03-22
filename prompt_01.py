# Reejecutamos porque se reinició el entorno. Volvemos a crear el archivo con el prompt actualizado.
nuevo_prompt_reestructurado = """
Actúa como un analista técnico profesional especializado en criptomonedas y genera un mensaje en español perfectamente estructurado para el canal de señales.

Objetivo: Crear la primera señal del día para Bitcoin (BTCUSD), basada en análisis técnico y fundamental. El mensaje debe ser motivador, organizado y visualmente atractivo.

Estructura exacta del mensaje (usa texto realista, no plantilla genérica):

1. Comienza con un saludo motivador tipo: “Buenos días traders! Qué mejor manera de comenzar el día que con nuestra primera señal del día. Hoy vamos a analizar Bitcoin y darles nuestras recomendaciones. ¡Vamos allá!”

2. Luego muestra:
𝐅𝐞𝐜𝐡𝐚: 22 de Marzo de 2025  
𝐒𝐞𝐧̃𝐚𝐥: 1 de 3

3. Agrega una breve descripción del trabajo del equipo:  
“Nuestro equipo trabaja arduamente para ofrecer análisis técnico y fundamental en tiempo real tres veces al día, asegurándonos de mantener a nuestra comunidad completamente informada y preparada.”

4. Lista de herramientas utilizadas con emoticones:
- Velas japonesas 📊
- Medias Móviles Exp 📈
- Fibonacci 🔢
- Fuerza Relativa (RSI) ⚖️
- (SQZMOM) ⚡️
- Volumen (POC) 💼

5. Sección: ◉ 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐓𝐞́𝐜𝐧𝐢𝐜𝐨:
Redacta un análisis técnico utilizando las herramientas anteriores, incluyendo observaciones claras en viñetas como:
📊 Velas: [...]
📈 EMAs: [...]
🔁 Fibonacci: [...]
🧱 POC: [...]
⚡️ RSI: [...]
🚀 SQZMOM: [...]

6. Sección: ◉ 𝐀𝐧𝐚́𝐥𝐢𝐬𝐢𝐬 𝐅𝐮𝐧𝐝𝐚𝐦𝐞𝐧𝐭𝐚𝐥:
💵 DXY: [...]
🧠 Sentimiento: [...]
📈 Nasdaq/SP500: [...]

7. Sección: ◉ 𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧 (𝐋𝐨𝐧𝐠 𝟑𝐱):
Redacta esta sección con datos reales:
💰 Entrada óptima entre: [rango mínimo] y [rango máximo]  
🎯𝐑𝐚𝐧𝐠𝐨 𝐝𝐞 𝐨𝐩𝐞𝐫𝐚𝐜𝐢𝐨́𝐧: Entre [rango calculado]
🟢 Porcentaje de efectividad estimado: 78%  
Condiciones ideales para una operación intradía de alta probabilidad.  
⚠️ ¡Cuida tu gestión de riesgo! No te olvides de establecer una estrategia de salida. Este mercado es altamente volátil. Operación recomendada solo para hoy.

8. Cierra con el bloque de promoción:
📊 Señales, gráficos en vivo y análisis en tiempo real completamente GRATIS por 30 días.  
🔑 𝐎𝐛𝐭𝐞́𝐧 𝐭𝐮 𝐦𝐞𝐬 𝐠𝐫𝐚𝐭𝐢𝐬 𝐚𝐡𝐨𝐫𝐚! 🚀  
Gracias por elegirnos como tu portal de trading de confianza. ¡Juntos, haremos que tu inversión crezca!  
✨ 𝐂𝐫𝐲𝐩𝐭𝐨 𝐒𝐢𝐠𝐧𝐚𝐥 𝐁𝐨𝐭 ✨Mantente pendiente del mensaje de mitad de sesión. ¡Feliz trading!
"""

# Guardar prompt reestructurado
prompt_path = "/mnt/data/prompt_01_reestructurado.txt"
with open(prompt_path, "w", encoding="utf-8") as f:
    f.write(nuevo_prompt_reestructurado.strip())

prompt_path
