#este programa verifica qual se são iguais e/ou maior ou menor
num1=float(input('digite um numero : '))
num2=float(input('digite o segundo numero:'))
if num1==num2:
    print('os numeros são iguais. ')
elif num1>num2:
    print('este numero',num1,'é maior que ',num2)
elif num2>num1:
    print('este numero',num2,'é maior que ',num1)