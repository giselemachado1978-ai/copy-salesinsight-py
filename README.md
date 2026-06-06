# SalesInsight PY

## Grupo de trabalho: Gisele dos Santos Machado / Herbert Martins Cardozo / Susej Gonzalez

## Sobre o projeto

O SalesInsight PY é um pipeline completo de análise de dados de vendas desenvolvido em Python.
O sistema lê, limpa, transforma e visualiza um dataset de vendas, gerando métricas, segmentações e projeções simples de tendência.

Neste projeto, criamos um analisador de dados de vendas com pipeline de análise preditiva simples com as seguintes etapas: coletar, limpar, transformar e visualizar dados, identificar padrões e gerar insights acionáveis a partir de um dataset.

Criamos um Kanban para visualizar e acompanhar o progresso das tarefas, e o GitHub Flow com branches descritivas, commits com mensagens claras e histórico que reflete a evolução lógica do trabalho.

O sistema analisa:

Receita total e volume de vendas por mês e trimestre
Top produtos e categorias por receita
Desempenho por região
Segmentação de clientes por nível de gasto (Bronze, Prata, Ouro)
Projeção simples de tendência para os próximos meses
Exportação de relatórios em CSV e JSON

### Stack:

```
VS Code
pandas
numpy
matplotlib
seaborn
ipykernel
notebook jupyter
```

## Como rodar o projecto

Clonar o Projeto

```
git clone https://github.com/HerbCyor/salesinsight-py.git
```

Criar um ambiente virtual dedicado

```
cd salesinsight-py

python -m venv .venv
```

Ativar o ambiente

```
source .venv/bin/activate (linux/macOS)
venv\Scripts\activate (windows)
```

Instalar as dependências

```
pip install -r requirements.txt
```

Rodando o pipeline

```
python ./src/main.py
```

Ou

```
cd src
python main.py
```

Também é possivel seguir a visualização passo a passo no jupyter notebook:

```
salesinsight/src/salesinsight.ipynb
```

# As etapas:

#### Etapa 1 - Criando o dataset de vendas

> Utilizamos uma helper function de um arquivo separado (gerador_dataset.py) para gerar um dataset na forma Dicionário python.

#### Etapa 2 - Inspecionando e exibindo as informações no dataset

> Funções básicas do Pandas para caracterizar o dataset
> df.shape() , df.columns(), df.dtypes()

_Nota 1: Utilizando o codigo modelo, foi necessario corrigir a identação e chamar a função df_bruto para impressao_

#### Etapa 3 - Limpeza e tratamento dos dados

> Remover ou imputar linhas com valores nulos nas colunas críticas (quantidade, preco_unitario);
> Remover linhas com datas inválidas (ex.: "DATA INVÁLIDA");
> Converter a coluna de data para o tipo datetime;
> Remover espaços extras em colunas de texto com .str.strip();
> Registrar no console quantos registros foram removidos.

_Nota 2: Foi necessário chamar a função para exibir o relatório. Também, anulou-se a função import re, sem uso neste bloco, e geramos nova inspeção do relatório, agora limpo._

#### Etapa 4 - Criando colunas derivadas com transformações

O objetivo deste bloco é enriquecer o dataset para análise gerando novas colunas a partir do dados existentes:

> receita_total: quantidade \* preco_unitario
> mes: mês extraído da data (número ou nome)
> trimestre: trimestre do ano (Q1, Q2, Q3, Q4)
> ano: ano extraído da data
> faixa_receita_item: classificação da receita por item usando transformação condicional

_Nota 3: Necessário acrescentar o comando de execução da função ao final, como no bloco anterior_

#### Etapa 5 - Calculo de métricas agrupadas

> Receita total e quantidade vendida por mês;
> Receita total por produto (top 5);
> Receita total por categoria;
> Receita total por região.

_Nota 4: comando de execução incluído_

#### Etapa 6 - Classificando clientes

> Agrupamos os dados por cliente, calculando o total gasto por cada e classificando-os em segmentos utilizando uma função lambda e uma transformação condicional.
> Critérios de classificação:
> Abaixo de R$ 5.000 --> Bronze
> R$ 5.000 a R$ 15.000 --> Prata
> Acima de R$ 15.000 --> Ouro"""

_Nota 5: Necessário incluir o comando que chama e executa a função._

#### Etapa 7 - Calculando estatatísticas com o Numpy

> Usamos o NumPy para:
>
> Conversão de uma coluna do DataFrame para array NumPy;
> Uso de operações vetorizadas (sem loops);
> Uso de broadcasting ou operações entre arrays;
> Demonstração das funções NumPy, mean, std, median, percentile, sum, etc.

_Nota 6: Inclusao da linha de codigo que chama e executa a função._

#### Etapa 8 - Gerando gráficos com MATPLOTLIB E SEABORN

> Este bloco gera e salva em PNG, gráficos informativos, com título, rótulos de eixos e legenda, tais como:
>
> Gráfico de linha: Receita total por mês ao longo do tempo;
> Gráfico de barras: Top 5 produtos ou categorias por receita;
> Gráfico de boxplot: Distribuição por região.

#### Etapa 9 - Criando uma classe para o Pipeline

> Criamos uma classe que encapsule parte do pipeline e contém o contrutor (**init**), atributos e métodos que usem self.

_Nota 7: Necessário criar uma instance e incluir comando para rodar o codigo passo a passo e exibir o relatório._

#### Etapa 10 - Demonstração do uso do conceito de Herança

> Como uma classe pode herdar de outra classe e receber novas funcionalidades.

_Nota 8: Necessário criar uma instance e incluir metodos de projeção._

#### Etapa 11 - Usando Funções Lambda e Funções de Ordem Superior

> Uso de funções lambda e demonstração de uma função que recebe outra como parâmetro (equivalente ao conceito de callback)

#### Etapa 12 - Leitura e criação de arquivos CSV e JSON

_Nota 9: Necessario incluir a linha de codigo de execução para exibir o resultados e o arquivo Json_

#### Etapa 13 - Utilizando expressoes regulares para limpeza de dados

> Aqui é necessário importar e usar o módulo re para executar a limpeza ou validação de dados com expressões regulares

#### Etapa 14 - Executando o pipeline completo

> Este bloco principal executa todo o pipeline de ponta a ponta, demonstrando o uso da classe e de todas as funções criadas.

"LINK PARA O VIDEO"
