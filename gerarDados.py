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

if ano.isnumeric() and (len(ano)==4) and 1960<=int(ano)<2024:
    #transformando a variavel ano em inteiro para operações: 
    ano=int(ano)
else: 
    print("Você não respeitou as condições para gerar dados!")
    print("Por favor, tente novamente respeitando as seguintes intruções: ")
    print("- Ano tem que ser composto apenas de números")
    print("- Tem que ter necessariamente 4 digitos! exemplo; 1990")
    print("- Deve necessariamente ser do intervalo de 1960 até 2023")
    ano = input("Tente novamente digitar o ano, seguindo as instruções: ")
    if ano.isnumeric() and (len(ano)==4) and 1960<=int(ano)<2024:
    #transformando a variavel ano em inteiro para operações: 
        ano=int(ano)
    else:
        print("Condições não respeitadas, fim da execução do programa")
        exit()

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
num_lojas=1000
estados = ["Amazonas", "Pará", "Roraima", "Amapá", "Rondônia", "Acre", "Tocantins",
           "Piauí", "Maranhão", "Pernambuco", "Rio Grande do Norte", "Paraíba", "Ceará", "Bahia", "Alagoas", "Sergipe",
           "Mato Grosso", "Mato Grosso do Sul", "Goiás",
           "São Paulo", "Rio de Janeiro", "Espírito Santo", "Minas Gerais",
           "Rio Grande do Sul", "Paraná", "Santa Catarina"]

#estipulando metas: 
metas = [7000, 7200, 7500, 7800, 8000, 8200, 8500]
#Laço para gerar nome de lojas e gerar aleatoriamente estado e região: 

if os.path.isfile('dados_de_lojas.txt'):
    pass
else: 
    dadosloja= open("dados_de_lojas.txt","w")
    cabeca = "Loja, Estado, Região, Meta de Vendas \n"
    dadosloja.write(cabeca)
    for n in range(num_lojas):
        i = random.randint(0,25)
        k = random.randint(0,6)
        if 0 <= i < 7:
            regiao = "Norte"
        elif 7<= i < 16:
            regiao = "Nordeste"
        elif 16<= i < 19:
            regiao = "Centro-Oeste"
            
        elif 19<= i <23:
            regiao = "Sudeste"
        elif 23<= i <26:
            regiao = "Sul"
        else: 
            pass
        
        info_lojas = "Loja " + str(n+1)+ ", " + estados[i] + ", " + regiao + ", " + str(metas[k]) + "\n"
        dadosloja.write(info_lojas)
        dadosloja.closed

lojas = []
dadosloja= open("dados_de_lojas.txt","r")
for line in dadosloja:
    lojas.append(line.split(','))

dadosloja.closed
nome_loja = []
estado_loja = []
regiao_loja = []
meta_loja = []
for n in range (1, len(lojas)):
    nome_loja.append(lojas[n][0])
    estado_loja.append(lojas[n][1])
    regiao_loja.append(lojas[n][2])
    meta_loja.append(int(lojas[n][3]))



#Gerando os dados de 
for n in range(len(dias_meses)):
    qtd_dias = dias_meses[n]
    for i in range(1, qtd_dias+1):
        local = caminho[n] + str(i)+'_' + meses[n] + '_' + str(ano) + '.csv'
        print(local)
        with open(local, 'w', newline='') as arquivocsv:
            csv.writer(arquivocsv, delimiter=',').writerow(['Loja', 'Estado', 'Região', 'Valor vendido', 'Meta de Vendas'])

            for j in range(len(nome_loja)):
                vendas = random.uniform(6000, 10000)
                csv.writer(arquivocsv, delimiter=',').writerow([nome_loja[j], estado_loja[j], regiao_loja[j], str(round(vendas, 2)), str(meta_loja[j])])
                arquivocsv.closed
