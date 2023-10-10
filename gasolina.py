import seaborn as sns
import pandas as pd
data = pd.read_csv('gasolina.csv')

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=data, x="dia",  y="venda", palette="dark")
  grafico.set(title='Valor da gasolina em: 07/2021', xlabel='Dia',  ylabel='Preço(USD)');