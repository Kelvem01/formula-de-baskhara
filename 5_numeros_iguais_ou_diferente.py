#este programa verifica se tem algum numero repetido
num1=float(input('digite o 1° numero: '))
num2=float(input('digite o 2° numero: '))
num3=float(input('digite o 3° numero: '))
num4=float(input('digite o 4° numero: '))
if num1==num2 or num1==num3 or num1==num4 or num2==num3 or num2==num4 or num3==num4:
    print("numeros iguais")
else:
    print("não há numeros repetidos! ")
    print("fim do programa...")