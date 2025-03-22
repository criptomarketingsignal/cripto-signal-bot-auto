import os
from flask import Flask
from prompt_01 import send_prompt_01

app = Flask(__name__)

@app.route('/')
def home():
    return 'Cripto Signal Bot API activa'

@app.route('/test')
def test():
    send_prompt_01()
    return 'Señal enviada correctamente'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

