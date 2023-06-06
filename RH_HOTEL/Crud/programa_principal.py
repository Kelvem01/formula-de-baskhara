# Kelvem ferreira da silva
# Fabio Fernandes Elias
# Trabalho crud umc

# impostrando sql para obter o banco de dados
import sqlite3
from funcoes_crud import *
conn = sqlite3.connect('Crud_umc.sqlite3')

# mostrando as opções do programa
print("""
    [1] Realizar cadastro
    [2] mostrar cadastro POR ID 
    [3] mostrar todos os cadastros
    [4] Atualizar cadastro
    [5] Deletar cadastro
    [0] Finalizar programa """)

# looping com while para melor desenpenho
while True:
    op = input('Digite a opção desejada: ')
    if op == '0':
        print('Programa finalizado! ')
        break
    elif op == '1':
        cadastro(conn)
    elif op == '2':
        mostrar_cadastro(conn)
    elif op =='3':
        mostra_todos_cad(conn)
    elif op == '4':
        atualizar_cad(conn)
    elif op =='5':
        deletar_cad(conn)
    else:
        print('opção invalida! ')
# comitando e fechando a conecção 
    conn.commit()
    conn.close()