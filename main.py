from flask import Flask, request, jsonify
import json
import tensorflow as tf
from chatbot.bot import identificar_intencao

app = Flask(__name__)

# Carregar o modelo de IA
model = tf.keras.models.load_model('models/modelo.h5')

# Rota para prever a categoria de um gasto
@app.route('/prever', methods=['POST'])
def prever():
    dados_transacao = request.json
    categoria_prevista = prever_categoria(dados_transacao)
    return jsonify({'categoria': categoria_prevista})

# Rota para interagir com o chatbot
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = identificar_intencao(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
