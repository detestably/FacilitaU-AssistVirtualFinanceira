import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from preprocess import preprocess_texts

# Exemplo de dados de treinamento
transacoes = [
    ("gastei 20 reais no uber", "transporte"),
    ("pedi um ifood por 35 reais", "fastfood"),
    ("fui ao cinema e gastei 50 reais", "lazer"),
    ("paguei 200 reais de aluguel", "moradia"),
    ("comprei um livro por 40 reais", "educacao")
]

# Preparação dos dados
sentences, labels = zip(*transacoes)
X, tokenizer = preprocess_texts(sentences)

# Mapeando categorias para números
label_map = {"transporte": 0, "fastfood": 1, "lazer": 2, "moradia": 3, "educacao": 4}
y = np.array([label_map[label] for label in labels])

# Dividindo os dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando a rede neural
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=16, input_length=X.shape[1]),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(len(label_map), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Treinando o modelo
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Salvando o modelo e o tokenizer
model.save("models/modelo.h5")
np.save("models/tokenizer.npy", tokenizer.word_index)
print("Modelo treinado e salvo com sucesso!")
