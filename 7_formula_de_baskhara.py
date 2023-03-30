#este programa resolve a formula do baskhara
c_a=int(input('digite um numero para o coeficiente a:'))
c_b=int(input('digite um numero para o coeficiente b:'))
c_c=int(input('digite um numero para o coeficiente c:'))
#primeiro resulvemos o delta
delta = (c_b ** 2) -4*c_a*c_c
#esta impresão e para fazer uma linha de espaço
print('\n**************************************\n')
if c_a ==0:
    print('o valor do coeficiente (a) deve diferente de  0. ')
elif delta < 0:
    print(' sem raizes reais .')
else:
    x1=(-c_b + delta ** (1/2) ) / (2*c_a)
    x2=(-c_b - delta ** (1/2) ) / (2*c_a)
    print('o resultado é ', x1 ,'e', x2)