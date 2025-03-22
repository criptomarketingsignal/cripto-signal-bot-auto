from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from prompts.prompt_01 import send_prompt_01

app = Flask(__name__)
scheduler = BackgroundScheduler()

# Envío automático a las 9:30 a.m. EST (13:30 UTC)
scheduler.add_job(send_prompt_01, 'cron', hour=13, minute=30)

scheduler.start()

@app.route("/")
def home():
    return "Crypto Signal Bot is running."

# Ruta manual para probar el mensaje
@app.route("/test")
def test_signal():
    send_prompt_01()
    return "✅ Señal enviada a ambos canales."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

