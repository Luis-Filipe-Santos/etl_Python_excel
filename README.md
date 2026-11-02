# Profiling e validação de dados de campanhas de anúncios

Lê um CSV de campanhas de anúncios, gera um relatório de profiling em HTML e define o schema de validação das colunas com Pydantic.

Stack: Python, pandas, ydata-profiling e Pydantic.

## O que faz hoje

- `main.py` lê `dados.csv` (cerca de 2,7 mil linhas), gera o relatório com o ydata-profiling e salva em `output.html`.
- `validador.py` define o schema das 14 colunas, com tipos e limites, usando Pydantic.

Colunas: Organizador, Ano_Mes, Dia_da_Semana, Tipo_Dia, Objetivo, Date, AdSet_name, Amount_spent, Link_clicks, Impressions, Conversions, Segmentação, Tipo_de_Anúncio e Fase.

## Dados

Origem: [PREENCHER: origem do dataset e licença]. Se os dados vierem de uma empresa ou de um cliente, remova os arquivos do repositório.

`dados_2025.csv`: [PREENCHER: o que é este arquivo].

## Como rodar

```bash
pip install -r requirements.txt
python main.py
```

Abra `output.html` no navegador.

## Limitações conhecidas

- O `main.py` não chama o `validador.py`, então as linhas do CSV ainda não passam pela validação.
- O projeto não lê nem escreve arquivos Excel.
