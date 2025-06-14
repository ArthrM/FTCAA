# Estudo Comparativo de Algoritmos de Busca
## Relatório Técnico

### Nome: Arthur José Silva Maluf
### RA: 22005252

## 1. Introdução

### 1.1 Objetivo do Estudo
Este estudo tem como objetivo comparar o desempenho de dois algoritmos de busca: busca sequencial e busca binária. A análise será realizada considerando diferentes tamanhos de entrada e cenários de uso, com foco em métricas de tempo de execução e número de comparações realizadas.

### 1.2 Algoritmos Implementados

#### 1.2.1 Busca Sequencial
A busca sequencial percorre a lista elemento por elemento até encontrar o valor desejado ou chegar ao final da lista. Sua implementação é direta e não requer que a lista esteja ordenada.

#### 1.2.2 Busca Binária
A busca binária é um algoritmo mais eficiente que aproveita a ordenação da lista para reduzir o espaço de busca pela metade a cada iteração. Ela compara o elemento buscado com o elemento central da lista e, com base nessa comparação, descarta metade dos elementos restantes.

### 1.3 Complexidade de Tempo
- Busca Sequencial: O(n)
- Busca Binária: O(log n)

## 2. Metodologia

### 2.1 Hardware Utilizado
- Processador: 

	Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz

	Velocidade base: 2,59 GHz
	Sockets: 1
	Núcleos: 6
	Processadores lógicos: 12
	Virtualização: Habilitado

- Memória RAM:

	16,0 GB

	Velocidade: 2667 MT/s
	Slots usados: 2 de 2
	Fator forma: SODIMM
	Reservada para hardware: 187 MB

- Sistema Operacional: 

    Edição: Windows 11 Home Single Language
    Versão: 23H2
    Instalado em: 21/11/2022
    Compilação do SO: 22631.5335
    Experiência: Pacote de Experiência de Recursos do Windows 1000.22700.1081.0

### 2.2 Linguagem de Programação
Python 3.8+

### 2.3 Repositório de Código
https://github.com/ArthrM/FTCAA

### 2.4 Metodologia Experimental
Para garantir robustez estatística, cada cenário de teste (combinação de algoritmo, tamanho de entrada e tipo de caso) foi executado 50 vezes. Foram coletados os tempos de execução (em milissegundos) e o número de comparações de cada execução. Os gráficos apresentam a média e o desvio padrão (barras de erro) dos resultados.

**Observação sobre precisão de tempo:**
Para medições de tempo, foi utilizado o `time.perf_counter()` do Python, que oferece maior precisão para intervalos curtos em comparação ao `time.time()`. Isso é importante porque, para algoritmos muito rápidos como a busca binária, o tempo de execução pode ser tão pequeno que métodos menos precisos registram valores próximos de zero. O uso do `perf_counter()` permite capturar diferenças sutis e obter resultados mais confiáveis.

## 3. Resultados

### 3.1 Tabelas de Resultados

Os valores abaixo representam as médias das 50 execuções para cada cenário. O desvio padrão está representado nos gráficos por barras de erro.

#### Caso Médio
| Tamanho | Algoritmo   | Tempo Médio (ms) | Desvio Tempo (ms) | Comparações Médias | Desvio Comparações |
|---------|-------------|------------------|-------------------|--------------------|--------------------|
| 1.000   | Sequencial  | 0.0287           | 0.0169            | 542,32             | 282,23             |
| 10.000  | Sequencial  | 0.3837           | 0.2753            | 5.089,92           | 2.682,79           |
| 100.000 | Sequencial  | 3.1860           | 2.2775            | 46.143,28          | 25.990,47          |
| 1.000   | Binária     | 0.0021           | 0.0004            | 9,14               | 1,18               |
| 10.000  | Binária     | 0.0039           | 0.0011            | 12,36              | 1,41               |
| 100.000 | Binária     | 0.0054           | 0.0012            | 15,84              | 1,72               |

#### Pior Caso
| Tamanho | Algoritmo   | Tempo Médio (ms) | Desvio Tempo (ms) | Comparações Médias | Desvio Comparações |
|---------|-------------|------------------|-------------------|--------------------|--------------------|
| 1.000   | Sequencial  | 0.0550           | 0.0026            | 1.000,00           | 0,00               |
| 10.000  | Sequencial  | 0.6310           | 0.1545            | 10.000,00          | 0,00               |
| 100.000 | Sequencial  | 6.2355           | 0.7665            | 100.000,00         | 0,00               |
| 1.000   | Binária     | 0.0020           | 0.0002            | 10,00              | 0,00               |
| 10.000  | Binária     | 0.0035           | 0.0007            | 14,00              | 0,00               |
| 100.000 | Binária     | 0.0055           | 0.0009            | 17,00              | 0,00               |

### 3.2 Gráficos Comparativos
Os gráficos gerados (`tempo_execucao.png` e `comparacoes.png`) apresentam:
- Eixo X: Tamanho da entrada (apenas 1000, 10000 e 100000)
- Eixo Y: Tempo médio de execução (em milissegundos) ou número médio de comparações
- Linhas sólidas: Caso médio; Linhas tracejadas: Pior caso
- Barras de erro: Desvio padrão das 50 execuções
- Todas as linhas dos algoritmos e casos estão presentes

**Análise visual dos gráficos:**

- O gráfico de tempo de execução mostra claramente que a busca sequencial tem crescimento linear tanto no caso médio quanto no pior caso, com o pior caso sempre acima do caso médio. A variação (barras de erro) aumenta com o tamanho da entrada, especialmente no caso médio, refletindo a aleatoriedade da posição do elemento.
- A busca binária, por outro lado, apresenta tempos extremamente baixos e praticamente constantes, tanto no caso médio quanto no pior caso, mesmo para 100.000 elementos. As barras de erro são quase imperceptíveis, indicando alta estabilidade e previsibilidade do algoritmo.
- No gráfico de número de comparações, a busca sequencial novamente cresce linearmente, enquanto a busca binária cresce de forma logarítmica, mantendo-se em valores muito baixos. O caso médio da busca sequencial apresenta maior variação, enquanto o pior caso é constante (igual ao tamanho da entrada).
- A separação visual entre as linhas azul (sequencial) e laranja (binária) evidencia a superioridade da busca binária em termos de eficiência, especialmente para grandes volumes de dados.

Esses gráficos ilustram de forma clara e didática a diferença de complexidade entre os algoritmos, validando a análise teórica apresentada anteriormente.

### 3.3 Análise dos Resultados
Os resultados obtidos confirmam a análise teórica da complexidade dos algoritmos:

1. **Busca Sequencial**:
   - Tempo de execução cresce linearmente com o tamanho da entrada
   - No pior caso, realiza exatamente n comparações
   - No caso médio, realiza aproximadamente n/2 comparações
   - Maior variação nos tempos devido à natureza sequencial

2. **Busca Binária**:
   - Tempo de execução praticamente constante e muito baixo
   - Número de comparações cresce muito lentamente (logaritmicamente)
   - Baixa variação nos tempos e comparações
   - Mantém desempenho excelente mesmo com entradas grandes

## 4. Conclusão

### 4.1 Análise Crítica
A busca binária demonstrou ser significativamente mais eficiente que a busca sequencial em todos os cenários testados. A diferença de desempenho se torna mais evidente conforme o tamanho da entrada aumenta. O uso de múltiplas execuções e barras de erro reforça a robustez dos resultados.

### 4.2 Vantagens e Limitações
- **Busca Sequencial**:
  - Vantagens: Simples de implementar, não requer ordenação
  - Limitações: Desempenho linear, ineficiente para grandes conjuntos de dados

- **Busca Binária**:
  - Vantagens: Extremamente eficiente, número de comparações logarítmico
  - Limitações: Requer dados ordenados, implementação mais complexa

### 4.3 Reflexão sobre a Importância da Complexidade
Os resultados demonstram a importância crucial de considerar a complexidade dos algoritmos na escolha da solução. Para conjuntos de dados grandes, a diferença de desempenho entre O(n) e O(log n) é dramática, podendo significar a diferença entre uma aplicação responsiva e uma inutilizável.

## 5. Bibliografia

1. PDFs de Fundamentos da Computação e Análise de Algoritmos (FTCAA) – Prof. José Guilherme Picolo, plataforma Canvas, PUCCAMP, 2025.
2. Python Software Foundation. (2025). Python 3.12.2 Documentation 