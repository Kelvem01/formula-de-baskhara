# programa para classe eleitoral


#entrada de dados 
nome = input('Digite seu nome : ')

idade = int (input(" Digete sua idade! "))

#looping do programa com while 
while True:
    if idade >=0 and idade <=15:
        print(f'{nome}  você é um eleitor invalido!')

        tent = int(input('Deseja continuar? , (1)sim,(2)não: '))
        
        if tent == 1:
            idade = int (input(" Digete sua idade! "))
        else:
            print('fim do programa, até logo!')
            break

    elif idade >= 16 and idade <=17:
        print(f'{nome}  você é um eleitor facultativo !')

        tent = int(input('Deseja continuar? , (1)sim,(2)não: '))
        
        if tent == 1:
            idade = int (input(" Digete sua idade! "))
        else:
            print('fim do programa, até logo!')
            break

    elif idade >= 18 and idade <= 65:
        print (f'{nome}  você é um eleitor obrigatório!')

        tent = int(input('Deseja continuar? , (1)sim,(2)não: '))
        
        if tent == 1:
            idade = int (input(" Digete sua idade! "))
        else:
            print('fim do programa, até logo!')
            break
    
    elif idade >= 66 and idade <= 100:
        print (f'{nome}  você é um eleitor facultativo !')

        tent = int(input('Deseja continuar? , (1)sim,(2)não: '))
        
        if tent == 1:
            idade = int (input(" Digete sua idade! "))
        else:
            print('fim do programa, até logo!')
            break
    
    elif idade >= 101:
        print (f'{nome}  você é um eleitor invalido!')

        tent = int(input('Deseja continuar? , (1)sim,(2)não: '))
        
        if tent == 1:
            idade = int (input(" Digete sua idade! "))
        else:
            print('fim do programa, até logo!')
            break

