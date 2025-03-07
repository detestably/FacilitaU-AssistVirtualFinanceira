import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Carregar dados
data = pd.read_csv('data/transacoes.csv')

# Pré-processamento de dados (como normalização, tokenização, etc.)
# Aqui você pode incluir o código de pré-processamento específico

# Separar features e labels
X = data[['valor', 'categoria', 'data']]  # Exemplo
y = data['categoria']  # Exemplo

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Construir o modelo
model = Sequential([
    Dense(64, input_dim=X_train.shape[1], activation='relu'),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dense(len(y.unique()), activation='softmax')
])

# Compilar o modelo
model.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Treinar o modelo
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Salvar o modelo treinado
model.save('models/modelo.h5')
