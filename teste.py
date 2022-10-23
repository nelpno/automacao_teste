import csv
import pandas as pd

df = pd.read_excel('teste.xlsx') # can also index sheet by name or fetch all sheets
cliente_lista = df['Cliente'].tolist()
id = df['ID'].tolist()
valor = df['Valor'].tolist()
i = 0

print(type(valor))
def qual_cliente(i):
    cliente = cliente_lista[i]
    valor_investido = valor_lista[i]
    escrita_boleto = ("{}-{}".format(cliente, data_hoje()))
    return cliente, valor_investido

print(qual_cliente(0))