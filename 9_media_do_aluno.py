# este programa calcula a media do aluno 
p1=float(input('digite sua primeira nota : '))
p2=float(input('digite a segunda nota : '))
p3=float(input('digite a terceira nota : '))
p4=float(input('digite a quarta nota : '))
# calcula media 
media = (2 * p1 + 2 * p2 +3 * p3 + 3 * p4 )/ 10
if media >=7:
    print('você esta aprovado com a nota ',media)
elif media <=5:
    print('você esta reprovado com a nota ',media)
elif media ==6 or media <=7:
    exame=float(input('digite a nota do exame final : '))
    media_final= media+exame/2
    if media_final >=7:
        print('a sua media final é ', media_final,'você esta aprovado')
    else:
        media_final<=5
        print('você esta reprovado com a media final de ',media_final)
