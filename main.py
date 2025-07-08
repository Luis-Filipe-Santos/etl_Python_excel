# pandas para ler CSV e transformar em dataframe
import pandas as pd
from ydata_profiling import ProfileReport  # se for pandas_profiling, adapte

# Lê os dados primeiro
df = pd.read_csv('dados.csv')

# Gera o relatório com o dataframe já carregado
profile = ProfileReport(df, title="Profiling Report", explorative=True)

# Salva o relatório em HTML
profile.to_file("output.html")
