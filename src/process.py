import pandas as pd

# Função para pré-processar os dados
def preprocessar_dados(data):
    # Exemplos de pré-processamento: conversão de data, normalização de valores, etc.
    data['data'] = pd.to_datetime(data['data'])
    data['valor'] = data['valor'] / data['valor'].max()  # Normalizando valores
    return data
