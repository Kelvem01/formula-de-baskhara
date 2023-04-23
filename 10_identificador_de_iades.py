#este programa diz se voce é criança , adolecente , adulto e idoso
idade=int(input('digite sua idade: '))
#processamento da idade 
if idade <= 12:
    print('sua idade é ',idade,'você é uma criança .')
elif idade <= 18:
    print('sua idade é ',idade,'você é um adolecente .')
elif idade <= 59:
    print('sua idade é ',idade,'você é um adulto .')
elif idade >= 59:
    print('sua idade é ',idade,'você é um idoso')
print('fim do programa')