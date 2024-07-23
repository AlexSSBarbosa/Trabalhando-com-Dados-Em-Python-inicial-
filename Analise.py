import pandas as pd
import os 
import matplotlib.pyplot as plt
import numpy as np

lista_df = []
nomes = []
diretorio = "./"

for ano in os.listdir(diretorio):
    if ano.isdecimal():
        cam_ano = diretorio + ano
        for mes in os.listdir(cam_ano):
            cam_mes = ano + "/" + mes
            for dia in os.listdir(cam_mes):
                if dia.endswith(".csv"):
                    nome_arquivo = "/" + dia
                    print(diretorio+"/"+ano+"/"+"/"+mes+nome_arquivo)
                    nome_df = pd.read_csv(diretorio+"/"+ano+"/"+"/"+mes+nome_arquivo, sep=",", encoding="latin-1")
                    lista_df.append(nome_df)
                    x = dia.rfind(".")
                    nomes.append(dia[:x])
            cam_mes = ""
        cam_ano = ""

print(len(lista_df))

#arquivo concatenado:
df_concat = lista_df[0]
contador = 1
for i in lista_df[1:]:
 print("percentual carregado: " + str(round((contador*100)/len(lista_df), 2)) + "% de 100%")
 df_concat = pd.concat([df_concat, lista_df[contador]])
 contador +=1

#Vendas
total_vendas = df_concat.groupby('Loja')['Valor vendido'].sum()

top_10 = total_vendas.sort_values(ascending=False).head(10)

red_10 = top_10 = total_vendas.sort_values(ascending=False).tail(10)

total_vendas = df_concat['Valor vendido'].sum()





#Definindo posição para o grafico
posi = np.zeros(len(top_10))
posi[0] = 0.15
#Lista de cores dos graficos: 
lista_cores=['DodgerBlue', 'DarkOrange', 'green', 'red', 'purple', 'SaddleBrown', 'HotPink', 'Gray', 'LawnGreen', 'Aqua']



print(total_vendas)

#criando a figura e eixos para o gráfico: 
fig, ax = plt.subplots()
#Plotando o grafico: 
ax.pie(top_10,labels=top_10.index,
       colors=lista_cores,
      explode = posi,
       textprops={'fontsize': 5},
       autopct=lambda p: '{:.5f}%'.format(((sum(top_10)*p/100)/total_vendas)*100)
      )
plt.title("Percentual top 10 de lojas que mais venderam ")
plt.show()


#criando a figura e eixos para o gráfico: 
fig, ax = plt.subplots()
ax.pie(top_10,labels=top_10.index,
       colors=lista_cores,
      explode = posi,
       textprops={'fontsize': 5},
       autopct=lambda p: 'R$ {:.2f}'.format((sum(top_10)*p/100))
      )
plt.title("Total em reais da top 10 de lojas que mais venderam ")
plt.show()




#Red 10 lojas
#as 10 piores lojas da franquia em porcetagem de vendas e valor adquirido: 

#criando a figura e eixos para o gráfico: 
fig, ax = plt.subplots()
#Plotando o grafico: 
ax.pie(red_10,labels=red_10.index,
       colors=lista_cores,
      explode = posi,
       textprops={'fontsize': 5},
       autopct=lambda p: '{:.5f}%'.format(((sum(red_10)*p/100)/total_vendas)*100)
      )
plt.title("Percentual das 10 piores lojas da franquia:  ")
plt.show()


#criando a figura e eixos para o gráfico: 
fig, ax = plt.subplots()
ax.pie(red_10,labels=red_10.index,
       colors=lista_cores,
      explode = posi,
       textprops={'fontsize': 5},
       autopct=lambda p: 'R$ {:.2f}'.format((sum(red_10)*p/100))
      )
plt.title("Total em reais da das lojas que menos venderem na franquia")
plt.show()
