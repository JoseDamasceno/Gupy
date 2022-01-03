

#1) Observe o trecho de código abaixo:
#int INDICE = 13, SOMA = 0, K = 0;
#enquanto K < INDICE faça
#{
#K = K + 1;
#SOMA = SOMA + K;
#}]
#imprimir(SOMA);
#Ao final do processamento, qual será o valor da variável SOMA?
#------------------------

from io import StringIO
from os import truncate


def Questao1():
    INDICE = 13; SOMA = 0; K = 0

    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K
    print(SOMA)

#------------------------
#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor 
#sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
#escreva um programa na linguagem que desejar onde, informado um número, ele calcule a 
# sequência de Fibonacci e retorne uma  mensagem avisando se o número informado pertence ou não a sequência.

#def Questao2():
#    Digitado = imput('Digite um valor: ')

#    for Digitado < atual
#       posi[] = anterior + anterior
#       atual = atual + anterior
#    
#    Fibonacci[0,2]


def Questao2():

    valordigitado = int(input("Digite um numero : "))

    istrue = False
    n  = 20
    linha = [0] * n

    for l in range(n):  
        linha[0] = 0
        linha[1] = 1
        linha[l] = linha[l-1] + linha[l-2]                    
        if linha[l] == valordigitado:       
           istrue = True
    print('----------------------------------------------------')               
    print(linha)
    
    if istrue:
       print('----------------------------------------------------')    
       print('O Numero: '+format(valordigitado)+'  foi encontrado na sequência Fibonacci')    
       print('----------------------------------------------------')    
    else:
       print('----------------------------------------------------')    
       print('O Numero: '+format(valordigitado)+'  Não existe na sequência Fibonacci')    
       print('----------------------------------------------------')    
#Questao2()


#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

def Questao3():
    import json    
    valor = 0.00
    VendasAcimadaMedia = 0
    ValorMaiordoDia = 0.00    
    ValorMenordoDia = 0.00
    TotalValor =  0.00
    TotalDias = 0
    
    with open('C:/Users/DEV-01/Desktop/Adeilson/Jose/dados.json', encoding='utf-8') as fileJson:
        dados = json.load(fileJson)    
    
    for i in dados:   
        valor = i['valor']
        valor = round(valor,2)

        if  valor > 0:  
            TotalValor = TotalValor + valor
            TotalDias  = TotalDias + 1       
            

            if ValorMaiordoDia < valor:
               ValorMaiordoDia = valor
            
            if ValorMenordoDia == 0 or ValorMenordoDia > valor:
               ValorMenordoDia = valor          
    ValorMedio = TotalValor / TotalDias

    print('Maior Valor vendido R$: ',ValorMaiordoDia)        
    print('Menor Valor vendido R$: ',ValorMenordoDia)
    print('Valor Médio mensal vendido R$: ',ValorMedio)
    print('----------------------------------------------------------------------------------------------------------------')


    for i in dados:
      valor = i['valor']
      valor = round(valor,2)      
      if ValorMedio < valor and valor > 0:
         VendasAcimadaMedia  = VendasAcimadaMedia + 1
         print('O Faturamento do dia '+format((i['dia']))+' '+format(valor)+', foi maior que  a media Mensal:')   

    print('------------------------------------------------------------------------------------------------')        
    print('') 
    print('Quantidade de dias em que o faturamento foi maior que a media: '+format(VendasAcimadaMedia)+' dias')

#Questao3()

#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#SP – R$67.836,43
#RJ – R$36.678,66
#MG – R$29.229,88
#ES – R$27.165,48
#Outros – R$19.849,53

def Questao4():

    SP = 67836.43
    RJ = 36678.66
    MG = 29229.88
    ES = 27165.48
    Outros = 19849.53

    TotalGeral = SP+RJ+MG+ES+Outros   
    print(TotalGeral)  
    print('SP percentual de vendas: '+format(((SP/TotalGeral)*100))+'%')
    print('RJ percentual de vendas: '+format(((RJ/TotalGeral)*100))+'%')
    print('MG percentual de vendas: '+format(((MG/TotalGeral)*100))+'%')
    print('ES percentual de vendas: '+format(((ES/TotalGeral)*100))+'%')
    print('Outros Estados percentual de vendas: '+format(((Outros/TotalGeral)*100))+'%')


#Questao4()

#5) Escreva um programa que inverta os caracteres de um string.
def Questao5():    

    palavra = str(input("Digite uma palavra : "))
    nova_palavra = ''
    posi = len(palavra)

    while posi:
        posi -= 1                    
        nova_palavra += palavra[posi] 
    print(nova_palavra)

Questao5()    
