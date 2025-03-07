import pandas as pd
import tensorflow as tf

# Carregar o modelo treinado
model = tf.keras.models.load_model('models/modelo.h5')

# Função para prever categoria
def prever_categoria(dados_transacao):
    # Pré-processar os dados
    # Exemplo: normalizar, codificar dados, etc.
    dados = pd.DataFrame(dados_transacao)
    
    # Realizar a previsão
    previsao = model.predict(dados)
    categoria_prevista = previsao.argmax(axis=1)
    
    return categoria_prevista

# Exemplo de transação
transacao = [{'valor': 50, 'categoria': 'alimentacao', 'data': '2025-03-06'}]
categoria = prever_categoria(transacao)
print(f"A categoria prevista é: {categoria}")
