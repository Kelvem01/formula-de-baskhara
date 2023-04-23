'''Problema 02:

Elabore um algoritmo e respectivo código em Python que calcule o preço a pagar
 pelo fornecimento de energia elétrica e informe todos os dados 
 importantes ao usuário. O usuário deve entrar com a quantidade
 de kWh consumida e o tipo de instalação: R para residências,
 I para indústrias e C para comércios. O cálculo do preço a pagar deve
 ser feito de acordo com a tabela a seguir:'''





print('''Preço por tipo de faixa de consumo.
=================================================================================
Tipo                    Faixa (kWh)                  Preço por kWh

Residencial             Até 500 (inclusive)            R$  0,40
                        Acima de 500                   R$  0,65

---------------------------------------------------------------------------------
Comercial Até           1000 (inclusive)               R$ 0,55
                        Acima de 1000                  R$ 0,60

---------------------------------------------------------------------------------
Industrial 
                         Até 5000 (inclusive)          R$ 0,55 
                         Acima de 5000                 R$ 0,60
==================================================================================
''')

# tabela para calculo do consumo 
t1=0.40
t1_2=0.65
t2=0.55
t2_2=0.60
t3=0.55
t3_2=0.60


# entrada de dados para tipo e consumo do usuario
tipo = input('''digite o tipo que deseja saber o valor:

residencial ate 500 kwh :residencial 1
residencial acima de 500 kwh :residencial  2
comercial ate 500 kwh : comercial 1
comercial acima de 500 kwh: comercial 2
industrial ate 500 kwh : industrial 1
industrial acima de 500 kwh : industrial 2
''')
kwh = float (input('digite a quantidade consumida :'))

# processamento dos dados que o usuario forneceu 
if tipo == 'residencial 1':
    if kwh <= 500:
        valor1= kwh*t1
        print('o valor a ser pago é ,R$%.2f'%valor1)
elif tipo == 'residencial 2':
    if kwh >500:
        valor2=kwh*t1_2
        print('o valor a ser pago é R$%.2f'%
              valor2)
elif tipo == 'comercial 1':
    if kwh <=500:
        valor3_1=kwh*t2
        print('o valor a ser pago é R$%.2f'%valor3_1)
elif tipo == 'comercial 2':
    if kwh >500:
        valor3_2=kwh*t2_2
        print('o valor a ser pago é ,R$%.2f'%valor3_2)
elif tipo == 'industrial 1':
    if kwh <= 500 :
        valor4 = kwh*t3
        print('o valor a ser pago é ,R$%.2f'%valor4)
elif tipo=='industrial 2':
    if kwh>500:
        valor4_1=kwh*t3_2
        print('o valor a ser pago é R$%.2f'%valor4_1)
# caso o usuario use numeros o programa retorna informando o erro
else:
    tipo==(int)
    print('informações do tipo  invalidas')
print('fim do programa ')