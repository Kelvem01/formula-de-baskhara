'''Elabore um algoritmo e depois o respectivo programa em Python 
que calcule o reajuste de salário de um colaborador de uma empresa. 
Considere que o colaborador deve receber reajuste de 15% 
caso seu salário seja menor que R$1.500,00.
Se o salário for maior ou igual a R$1.500,00 
mas menor ou igual a R$ 4.000,00 seu reajuste deve ser de 10% ;
finalmente caso seu salário seja maior de R$4.000,00 o reajuste deve ser de 5%.'''


#este programa calcula o reajuste de salario dos funcionarios de acordo com o salario de cada um.
# entrada de dados 
salario=float(input('digite seu salario : '))
#processamento do reajuste de acordo com o salario do trabalhador 
if salario <1500:
    valor= salario * 15/100
    print("o valor de seu reajuste é de 15% , sendo total de ,R$",valor)
elif salario >= 1.500:
    valor2=salario*10/100
    print("o seu reajuste e de 10% , de acordo com seu salario ,total de R$",valor2)
elif salario <=4000:
    valor3=salario*10/100
    print("o valor é de 5%, do reajuste de acordo com seu salario e de R$",valor3)
else:
    salario > 4000
    valor4=salario*5/100
    print("o valor do seu reajuste é de 5%,de acordo com seu salario de R$",valor4)
print('fim do programa')

