# cadastro usuario

#importando sqlite3
import sqlite3
from fucao_rh import *
#fazendo conexão com banco de dados

conn = sqlite3.connect('RH_HOTEL.sqlite3')


 # entrada de dados dos clientes
while True:

    print('''Escolha a opção desejada:
      1) cadastro  
      2) preços 
      3) resevas
      4) mostrar cadastros
      5) mostrar reservas
      0) sair
      ''')
    opcao = input('digte a opção desejada: ')
    
    if opcao == '0':
        print('programa finalizado! ')
        break
    elif opcao =='1':
        cadastro_cliente(conn)
    
    elif opcao =='2':
        print('preços tabela 1 :')
        tabela_1()
        print('preços tabela 2 :')
        tabela_2()
    elif opcao =='3':
        cad_reserva(conn)
    elif opcao =='4':
        mostrar_clientes(conn)
    elif opcao == '5':
        mostrar_reservas(conn)
    
    else:
        print('opção invalida!')


conn.commit()
conn.close()

