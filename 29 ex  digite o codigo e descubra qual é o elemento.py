#29. Escreva um programa que leia o código de um determinado produto e mostre a sua
#classificação. Utilize a seguinte tabela como referências:

#codigo                     classificação

#1                         alimento nao prerecivel
#2  3  ou 4                 alimento prerecivel
#5 ou 6                      vestuariario
#7                           hiegiene pessoal
#8 até 15                    limpeza e utensileos domesticos
#qualquer outro codigo         invalido

idade = int(input("Digite um Codigo: "))

if idade <=1:  
        print ("alimento nao prerecivel\n")
elif idade <=4:
    print ("alimento prerecivel\n")
elif idade <=6:
    print ("vestuariario\n")
elif idade <=7:
    print ("hiegiene pessoal\n")
elif idade <=15:
    print ("limpeza e utensileos domesticos\n")
elif idade <=10000:
    print ("invalido\n")

