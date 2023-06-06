# Kelvem ferreira da silva
# Fabio Fernandes Elias
# Trabalho crud umc
import sqlite3
from funcoes_crud import *
conn = sqlite3.connect('Crud_umc.sqlite3')
print("""
    [1] Realizar cadastro
    [2] mostrar cadastro POR ID 
    [3] mostrar todos os cadastros
    [4] Atualizar cadastro
    [5] Deletar cadastro
    [0] Finalizar programa """)

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

    conn.commit()
    conn.close()