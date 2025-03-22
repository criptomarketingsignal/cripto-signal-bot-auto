from flask import Flask
from prompt_01 import send_prompt_01 as send_signal_1
from prompt_02 import send_prompt_01 as send_signal_2
from prompt_03 import send_prompt_01 as send_signal_3

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Crypto Signal Bot está activo y listo."

@app.route('/test')
def test_signal_1():
    send_signal_1()
    return "✅ Señal 1 de 3 enviada correctamente."

@app.route('/test2')
def test_signal_2():
    send_signal_2()
    return "✅ Señal 2 de 3 enviada correctamente."

@app.route('/test3')
def test_signal_3():
    send_signal_3()
    return "✅ Señal 3 de 3 enviada correctamente."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
