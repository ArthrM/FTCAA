# Estudo Comparativo de Algoritmos de Busca

Atividade complementar da disciplina de Teoria da Computação e Análise de Algoritmos da PUCCAMP, ministrada pelo Prof. José Guilherme Picolo. Aqui implementamos um estudo comparativo entre os algoritmos de busca sequencial e busca binária, analisando seu desempenho em diferentes cenários.

## Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Execução

Para executar o estudo comparativo, simplesmente execute o arquivo principal:

```bash
python busca_comparativa.py
```

## Resultados

O programa irá:
1. Executar os testes para diferentes tamanhos de entrada (1.000, 10.000 e 100.000 elementos)
2. Testar casos médios e piores casos
3. Gerar dois gráficos:
   - `tempo_execucao.png`: Comparação dos tempos de execução
   - `comparacoes.png`: Comparação do número de comparações realizadas
4. Gerar um arquivo CSV:
   - `resultados_busca.csv`: Contém as médias e desvios padrão dos tempos e comparações para cada cenário, facilitando a inclusão dos dados no relatório.

## Estrutura do Código

- `busca_comparativa.py`: Implementação dos algoritmos e lógica de teste
- `requirements.txt`: Dependências do projeto
- `README.md`: Este arquivo
- `resultados_busca.csv`: Resultados estatísticos das execuções (gerado automaticamente)

## Análise de Complexidade

- Busca Sequencial: O(n)
- Busca Binária: O(log n)

Onde n é o tamanho da entrada.
