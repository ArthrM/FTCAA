import random
import time
from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np
import csv

def busca_sequencial(arr: List[int], elemento: int) -> Tuple[int, int]:
    """
    Implementa a busca sequencial e retorna o número de comparações e o índice do elemento.
    Retorna (-1, comparações) se o elemento não for encontrado.
    """
    comparacoes = 0
    for i in range(len(arr)):
        comparacoes += 1
        if arr[i] == elemento:
            return i, comparacoes
    return -1, comparacoes

def busca_binaria(arr: List[int], elemento: int) -> Tuple[int, int]:
    """
    Implementa a busca binária e retorna o número de comparações e o índice do elemento.
    Retorna (-1, comparações) se o elemento não for encontrado.
    """
    comparacoes = 0
    esquerda, direita = 0, len(arr) - 1
    
    while esquerda <= direita:
        comparacoes += 1
        meio = (esquerda + direita) // 2
        
        if arr[meio] == elemento:
            return meio, comparacoes
        elif arr[meio] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1
            
    return -1, comparacoes

def gerar_array_ordenado(tamanho: int) -> List[int]:
    """Gera um array ordenado de números inteiros."""
    return sorted(random.sample(range(1, tamanho * 2), tamanho))

def executar_teste(tamanho: int, caso: str) -> dict:
    """
    Executa os testes para um determinado tamanho e caso.
    Retorna um dicionário com os resultados.
    """
    arr = gerar_array_ordenado(tamanho)
    
    if caso == "medio":
        elemento = random.choice(arr)
    else:  # pior caso
        elemento = max(arr) + 1
    
    # Teste busca sequencial
    inicio = time.perf_counter()
    _, comp_seq = busca_sequencial(arr, elemento)
    tempo_seq = (time.perf_counter() - inicio) * 1000  # milissegundos
    
    # Teste busca binária
    inicio = time.perf_counter()
    _, comp_bin = busca_binaria(arr, elemento)
    tempo_bin = (time.perf_counter() - inicio) * 1000  # milissegundos
    
    return {
        "tempo_sequencial": tempo_seq,
        "tempo_binaria": tempo_bin,
        "comparacoes_sequencial": comp_seq,
        "comparacoes_binaria": comp_bin
    }

def executar_estudo():
    """Executa o estudo completo e gera os gráficos."""
    tamanhos = [1000, 10000, 100000]
    casos = ["medio", "pior"]
    repeticoes = 50
    resultados = {algoritmo: {caso: {t: [] for t in tamanhos} for caso in casos} for algoritmo in ["sequencial", "binaria"]}
    comparacoes = {algoritmo: {caso: {t: [] for t in tamanhos} for caso in casos} for algoritmo in ["sequencial", "binaria"]}
    for tamanho in tamanhos:
        for caso in casos:
            for _ in range(repeticoes):
                res = executar_teste(tamanho, caso)
                resultados["sequencial"][caso][tamanho].append(res["tempo_sequencial"])
                resultados["binaria"][caso][tamanho].append(res["tempo_binaria"])
                comparacoes["sequencial"][caso][tamanho].append(res["comparacoes_sequencial"])
                comparacoes["binaria"][caso][tamanho].append(res["comparacoes_binaria"])
    gerar_graficos(resultados, comparacoes, tamanhos, casos, repeticoes)

def gerar_graficos(resultados, comparacoes, tamanhos, casos, repeticoes):
    """Gera os gráficos comparativos."""
    plt.figure(figsize=(10, 6))
    for algoritmo, cor, marcador in zip(["sequencial", "binaria"], ['tab:blue', 'tab:orange'], ['o', 's']):
        for caso, estilo in zip(casos, ['-', '--']):
            medias = [np.mean(resultados[algoritmo][caso][t]) for t in tamanhos]
            stds = [np.std(resultados[algoritmo][caso][t]) for t in tamanhos]
            label = f'{"Sequencial" if algoritmo=="sequencial" else "Binária"} ({caso})'
            plt.errorbar(tamanhos, medias, yerr=stds, fmt=marcador+estilo, color=cor, capsize=5, label=label)
    plt.xlabel('Tamanho da Entrada')
    plt.ylabel('Tempo de Execução (ms)')
    plt.title('Comparação de Tempo de Execução')
    plt.xticks(tamanhos, [str(t) for t in tamanhos])
    plt.legend()
    plt.grid(True)
    plt.savefig('tempo_execucao.png')
    plt.close()
    
    plt.figure(figsize=(10, 6))
    for algoritmo, cor, marcador in zip(["sequencial", "binaria"], ['tab:blue', 'tab:orange'], ['o', 's']):
        for caso, estilo in zip(casos, ['-', '--']):
            medias = [np.mean(comparacoes[algoritmo][caso][t]) for t in tamanhos]
            stds = [np.std(comparacoes[algoritmo][caso][t]) for t in tamanhos]
            label = f'{"Sequencial" if algoritmo=="sequencial" else "Binária"} ({caso})'
            plt.errorbar(tamanhos, medias, yerr=stds, fmt=marcador+estilo, color=cor, capsize=5, label=label)
    plt.xlabel('Tamanho da Entrada')
    plt.ylabel('Número de Comparações')
    plt.title('Comparação de Número de Comparações')
    plt.xticks(tamanhos, [str(t) for t in tamanhos])
    plt.legend()
    plt.grid(True)
    plt.savefig('comparacoes.png')
    plt.close()
    salvar_resultados_csv(resultados, comparacoes, tamanhos, casos, repeticoes)

def salvar_resultados_csv(resultados, comparacoes, tamanhos, casos, repeticoes):
    with open('resultados_busca.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Cenário', 'Tamanho', 'Algoritmo', 'Tempo Médio (ms)', 'Desvio Tempo (ms)', 'Comparações Médias', 'Desvio Comparações'])
        for algoritmo in ['sequencial', 'binaria']:
            for caso in casos:
                for t in tamanhos:
                    tempo_med = np.mean(resultados[algoritmo][caso][t])
                    tempo_std = np.std(resultados[algoritmo][caso][t])
                    comp_med = np.mean(comparacoes[algoritmo][caso][t])
                    comp_std = np.std(comparacoes[algoritmo][caso][t])
                    writer.writerow([
                        'Médio' if caso == 'medio' else 'Pior',
                        t,
                        'Sequencial' if algoritmo == 'sequencial' else 'Binária',
                        f'{tempo_med:.4f}',
                        f'{tempo_std:.4f}',
                        f'{comp_med:.2f}',
                        f'{comp_std:.2f}'
                    ])

if __name__ == "__main__":
    executar_estudo() 