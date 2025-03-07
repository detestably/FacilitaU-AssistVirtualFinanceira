import json
import random
import nltk
from nltk.stem import WordNetLemmatizer

# Carregar intents
with open('chatbot/intents.json') as file:
    intents = json.load(file)

# Inicializar lematizador
lemmatizer = WordNetLemmatizer()

# Função de pré-processamento do texto
def preprocessar_texto(texto):
    texto = texto.lower()
    palavras = nltk.word_tokenize(texto)
    palavras = [lemmatizer.lemmatize(palavra) for palavra in palavras]
    return palavras

# Função para identificar a intenção
def identificar_intencao(texto):
    palavras_processadas = preprocessar_texto(texto)
    # Comparar as palavras com as intents
    resposta = random.choice(intents['intents'][0]['responses'])  # Exemplo simples
    return resposta

# Exemplo de interação
print(identificar_intencao("Como posso controlar meus gastos?"))
