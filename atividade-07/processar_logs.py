import pandas as pd

def processar_logs(nome_arquivo):
    df = pd.read_csv(nome_arquivo)
    media_tempo = df['tempo_execucao'].mean()
    desvio_padrao = df['tempo_execucao'].std()
    print("Tempo de Execução:")
    print(f"Media: {media_tempo:.2f}")
    print(f"Desvio Padrão: {desvio_padrao:.2f}")

arquivo = input("Digite o nome do arquivo: ")
processar_logs(arquivo)