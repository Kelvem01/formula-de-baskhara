#este programa recebe 3 numeros consecutivos e diz se esta em orem crescente
#entrada de dados
num1=int(input('digite um numero: '))
num2=int(input('digite o 2° numero:  '))
num3=int(input('digite o 3° numero: '))

  #processamento dos numeros
if num1<num2 and num2<num3:
    print('numeros em ondem  crescente',num1,num2,num3)
else:
    print('não estão em  ordem crescente. ')
    print('fim do programa')