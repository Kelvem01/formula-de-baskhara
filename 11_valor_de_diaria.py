#este programa calcula a diaria de hospedagem por familia 

# tabela tipo 1 
t1_1=20.00
t1_2=28.00
t1_3=35.00
t1_4=42.00
t1_5=48.00
t1_6=53.00
# tabela tipo 2
t2_1=25.00
t2_2=34.00
t2_3=42.00
t2_4=50.00
t2_5=57.00
t2_6=63.00

#entrada de dados pro familia 
diaria = int(input('digite quantos dias deseja se hospedar, até 6 dias :'))
tipo = int(input('digite o tipo de hospedagem que deseja entre 1 e 2 :'))
pessoas= int(input('quantas pessoas ira se hospedar ? maximo 6. '))
# processamento de dados tipo 1 
if pessoas==1 and tipo ==1:
   valor1 = t1_1*diaria
   print('o valor a ser pago é ',valor1,' sua hospedagem é do tipo 1')
elif pessoas == 2 and tipo ==1:
   valor2 = t1_2*diaria
   print('o valor a ser pago é ',valor2,'sua hospedagem de do tipo 1')
elif pessoas ==3 and tipo ==1:
   valor3=t1_3*diaria
   print('o valor a ser pago é ',valor3,'sua hospedagem de do tipo 1')
elif pessoas == 4 and tipo ==1:
   valor4=t1_4*diaria
   print('o valor a ser pago é ',valor4,'sua hospedagem de do tipo 1')
elif pessoas == 5 and tipo == 1 :
   valor5= t1_5*diaria
   print('o valor a ser pago é ',valor5,'sua hospedagem de do tipo 1')
elif pessoas == 6 and tipo ==1:
   valor6=t1_6*diaria
   print('o valor a ser pago é ',valor6,'sua hospedagem de do tipo 1')
# processamento do tipo 2
elif pessoas ==1 and tipo ==2:
   valor1_t2=t2_1*diaria
   print('o valor a ser pago é ',valor1_t2,'sua hospedagem é do tipo 2 ')
elif pessoas ==2 and tipo ==2:
   valor2_t2= t2_2*diaria
   print('o valor a ser pago é ',valor2_t2,'sua hospedagem é do tipo 2 ')
elif pessoas ==3 and tipo == 2:
   valor3_t2= t2_3*diaria
   print('o valor a ser pago é ', valor3_t2,'sua hospedagem é do tipo 2 ')
elif pessoas ==4 and tipo ==2:
    valor4_t2=t2_4*diaria
    print('o valor a ser pago é ',valor4_t2,'sua hospedagem é do tipo 2 ')
elif pessoas ==5 and tipo ==2:
   valor5_t2=t2_5*diaria
   print('o valor a ser pago é ',valor5_t2,'sua hospedagem é do tipo 2 ')
elif pessoas ==6 and tipo ==2:
   valor6_t2 = t2_6*diaria
   print('o valor a ser pago é ',valor6_t2,'sua hospedagem é do tipo 2 ')