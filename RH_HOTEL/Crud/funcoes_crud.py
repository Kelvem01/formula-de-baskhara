# Kelvem ferreira da silva
# Trabalho crud umc

# criando funções para gerar um programa dinamico
import sqlite3
import datetime
# função de cadastro / create
def cadastro(conn):
    cursor = conn.cursor()

    nome = input('digite seu nome: ')
    cpf = input ('digite seu cpf: ')
    while True:
        senha = input('digite sua senha: ')
        conf_senha = input('confirme sua senha:')

        if conf_senha == senha:
            print('cadastro realizado com sucesso: ')
            break
        else:
            print('senha incorreta! ')
    sql ='INSERT INTO cadastro(nome ,cpf , senha) VALUES (?,?,?)'
    valores = [nome, cpf, senha]
    cursor.execute(sql, valores)
    
    conn.commit()
# função para mostrar cadastro / read
def mostrar_cadastro(conn):
    cursor = conn.cursor()
    id = input('digite o id do cadastro desejado: ')
    data = datetime.datetime.now()
    
    sql = f'SELECT * FROM cadastro WHERE id = {id}'

    dados = cursor.execute(sql)
    for dado in dados :
        print(f'ID:{dado[0]}',f'NOME:{dado[1]}',f'CPF:{dado[2]}',f'DATA:{data.strftime("%d/%m/%Y")}')
# função para mostrar todos os cadastros /read
def mostra_todos_cad(conn):
    cursor = conn.cursor()
    sql = 'SELECT * FROM cadastro'
    dados = cursor.execute(sql)

    for dado in dados:
        print(f'nome:{dado[1]}',f'cpf:{dado[2]}')
# função para atualizar cadastro /update
def atualizar_cad(conn):
    cursor = conn.cursor()

    id = input('Digite o ID desejado: ')
    nome = input('digite seu nome: ')
    cpf = input ('digite seu cpf: ')
    while True:
        senha = input('digite sua senha: ')
        conf_senha = input('confirme sua senha:')

        if conf_senha == senha:
            print('cadastro atualizado! ')
            break
        else:
            print('senha incorreta! ')

    sql = f""" UPDATE cadastro SET nome = '{nome}' , cpf = '{cpf}' , senha = '{senha}' WHERE id = {id} """
    
    cursor.execute(sql)
    conn.commit()
# função para deletar cadastro / delete
def deletar_cad(conn):
    cursor = conn.cursor()
    id = int(input('digite o id que deseja deletar: '))

    sql = f""" DELETE FROM cadastro WHERE id ={id}"""
    cursor.execute(sql)
    print('Cadastro deletado com sucesso! ')
    conn.commit()

