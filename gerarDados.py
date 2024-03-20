import os
import random
import csv

#iniciando o vetor com os dias de cada mês:
dias_meses = [31, 28, 31, 30, 31,30,31,31,30,31,30,31]
#iniciando um vetor com os meses do ano:
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
caminho = []
#Recebendo do terminal o ano para gerar os dados: 
ano = input("Digite um ano para gerar as informações aleatoriamente: ")

#transformando a variavel ano em inteiro para operações: 
ano=int(ano)

#Metodo para validar se o ano é bissexto 
def bissexto(ano):
    if ano%400==0 or (ano%4==0 and ano%100!=0):
        return 1
    else: 
        return -1

#bs recebe o retorno do metodo bissexto:
bs = bissexto(ano)
#compara se bs recebeu 1 para mudar a quantidade de dias do mês de fevereiro: 
if bs ==1:
    dias_meses[1] = 29

#valida se a pasta do ano já esta criada: Se sim, passa. Se não, cria: 
if os. path. isdir('./'+str(ano)):
    pass
else: os.mkdir('./'+str(ano))


#vetor para criar as pastas dos meses e adicionar o caminho na lista caminho:
for n in range(len(meses)):
    if (n+1)>=10:
        if os. path. isdir('./'+str(ano)+'/'+ str(n+1) + ' - ' + str(meses[n])):
            caminho.append('./'+str(ano)+'/'+ str(n+1) + ' - ' + str(meses[n]) + '/')
        else:
            os.mkdir('./'+str(ano)+'/'+ str(n+1) + ' - ' + str(meses[n]))
            caminho.append('./'+str(ano)+'/'+ str(n+1) + ' - ' + str(meses[n]) + '/')
    else: 
        if os. path. isdir('./'+str(ano)+'/'+ '0' + str(n+1) + ' - ' + str(meses[n])):
            caminho.append('./'+str(ano)+'/'+ '0' + str(n+1) + ' - ' + str(meses[n]) + '/')
        else:
            os.mkdir('./'+str(ano)+'/'+ '0' + str(n+1) + ' - ' + str(meses[n]))
            caminho.append('./'+str(ano)+'/'+ '0' + str(n+1) + ' - ' + str(meses[n]) + '/')

#Declaração de listas e variaveis para manipular os dados: 
lojas = []
endereco = []
regiao = []
num_lojas=1000
estados = ["Amazonas", "Pará", "Roraima", "Amapá", "Rondônia", "Acre", "Tocantins",
           "Piauí", "Maranhão", "Pernambuco", "Rio Grande do Norte", "Paraíba", "Ceará", "Bahia", "Alagoas", "Sergipe",
           "Mato Grosso", "Mato Grosso do Sul", "Goiás",
           "São Paulo", "Rio de Janeiro", "Espírito Santo", "Minas Gerais",
           "Rio Grande do Sul", "Paraná", "Santa Catarina"]


#Laço para gerar nome de lojas e gerar aleatoriamente estado e região: 
for n in range(num_lojas):
    lojas.append("Loja " + str(n+1))
    i = random.randint(0,25)
    endereco.append(estados[i])
    if 0 <= i < 7:
        regiao.append("Norte")
    elif 7<= i < 16:
        regiao.append("Nordeste")
    elif 16<= i < 19:
        regiao.append("Centro-Oeste")
    elif 19<= i <23:
        regiao.append("Sudeste")
    elif 23<= i <26:
        regiao.append("Sul")
    else: 
        pass

#estipulando metas: 
metas = [7000, 7200, 7500, 7800, 8000, 8200, 8500]

#Gerando os dados de 
for n in range(len(dias_meses)):
    qtd_dias = dias_meses[n]
    for i in range(1, qtd_dias+1):
        local = caminho[n] + str(i)+'_' + meses[n] + '_' + str(ano) + '.csv'
        print(local)
        with open(local, 'w', newline='') as arquivocsv:
            csv.writer(arquivocsv, delimiter=',').writerow(['Loja', 'Estado', 'Região', 'Valor vendido', 'Meta de Vendas'])

            for j in range(len(lojas)):
                vendas = random.uniform(6000, 10000)
                k = random.randint(0,6)
                meta = metas[k]
                csv.writer(arquivocsv, delimiter=',').writerow([lojas[j], endereco[j], regiao[j], str(round(vendas, 2)), str(meta)])
                arquivocsv.closed

        















