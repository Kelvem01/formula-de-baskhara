#este programa mostra a media de 2 numeros inteiros,
# tabem o quadrado de um numero float.
print('''
     este programa mostra a media de 2 numeros inteiros,
     -------------------------------------------------------
     também o quadrado de um numero real.

''')

desc = 0

print(''' 1) media , 2) numero ao quadrado, 0) sair :''')

desc = int (input('digite a opção desejada :'))


while desc != 0 :
    
    if desc == 1:
        num1 = float(input('digite o primeiro numero: '))
        num2 = int(input('digite o segundo numero: '))

        media = num1+num2/2
        
        print(f'os numeros escolhidos são {num1} e {num2} e a média é {media}')
        desc = int (input('''deseja realizar outra operação? :
        1) media 
        2) numero ao quadrado 
        0) sair'''))

    elif desc == 2:
        num = int(input('digite um numero'))

        valor = num**2

        print(f'o numero escolhido foi {num} ele ao quadrado é {valor}')
        desc = int (input('''deseja realizar outra operação? :
        ----------------------
        1) media 
        2) numero ao quadrado 
        0) sair
        ----------------------'''))


    elif desc == 0:
        print('fim do programa até logo!')

    else:
        print('opção invalida !')
        desc = int (input('''deseja realizar outra operação? :

        --------------------------
        1) media 
        2) numero ao quadrado 
        0) sair
        --------------------------'''))
    if desc == 0:

        print('fim do programa até logo!')
