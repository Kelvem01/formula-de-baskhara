#este programa recebe 2 numeros e realiza a divisão.
#se o segundo numero for 0 sera impossivel realizar a divisão

num1= int(input('digite um numero : '))
num2= int(input('digite o segundo numero : '))
if num2==0:
    print('não é possivel realizar a divisão por 0')
else:
    divisao=num1/num2
    print('o resultado é',divisao)
    print('programa finalizado!')