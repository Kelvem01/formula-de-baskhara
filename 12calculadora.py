'''Elabore um algoritmo e respectivo código em Python que leia 2 números e pergunte ao usuário
 qual operação se deseja realizar.
 O usuário deve poder calcular soma(+), subtração(-),
 multiplicação (*) ou divisão (/).
 Exiba o resultado da operação solicitada.'''

soma=1
subtracao=2
multiplicao=3
divisao=4

print('''
soma=1
subtracao=2
multiplicao=3
divisao=4 ''')

n1= float(input('digite um número. '))
n2= float(input('digite o segundo numero. '))
tipo_calculo=int(input('que tipo de calculo deseja realizar? '))
if tipo_calculo ==1:
    valor1 = n1+n2
    print('o valor é',valor1)
elif tipo_calculo==2:
    valor2 = n1-n2
    print('o valor é ',valor2)
elif tipo_calculo==3:
    valor3= n1*n1
    print('o valor é',valor3)
elif tipo_calculo==4:
    if n2 ==0:
        print('não é possivel realizar a divisão por 0')
    else:
        valor4= n1/n2
        print('o valor é ',valor4)
print('fim do programa ...')