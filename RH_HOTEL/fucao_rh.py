import sqlite3
import datetime
#função 1 tabela de preços

def tabela_1():
    print ('''
    quantidade de pessoas              diaria tipo 1
        no apartamento                  R$
        [1]                              R$ 20,00 
        [2]                              R$ 28,00
        [3]                              R$ 35,00
        [4]                              R$ 42,00
        [5]                              R$ 48,00
        [6]                              R$ 53,00''')
    
def tabela_2():
      print ('''
       quantidade de pessoas              diaria tipo 2
        no apartamento                  R$
        [1]                              R$ 25,00 
        [2]                              R$ 34,00
        [3]                              R$ 42,00
        [4]                              R$ 50,00
        [5]                              R$ 57,00
        [6]                              R$ 63,00
        ''')
      
def cadastro_cliente(conn):
    #criando cursor

    cursor = conn.cursor()
    nome = input ('Digite seu nome :')
    cpf = input('Digite seu CPF: ')
    email = input ('Digite seu email: ')


    # realizando validação de senha 
    while True:
        senha = int (input('Digite uma senha numerica :'))
        conf_senha = int(input ('confirme sua senha '))
        

        if conf_senha == senha :
            print('cliente cadastrado! ')
            break
        else :
            print ('senha incorreta !')
        
            

    sql = 'INSERT INTO cliente (nome, cpf, email, senha) values (?,?,?,?)'

    valores = [nome, cpf, email, senha]

    cursor.execute(sql,valores)
    conn.commit()

def cad_reserva(conn):
    cursor = conn.cursor()
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
    qtd_dias = int(input('digite quantos dias deseja se hospedar, até 6 dias :'))
    tipo = int(input('digite o tipo de hospedagem que deseja entre 1 e 2 :'))
    qtd_pessoas= int(input('quantas pessoas ira se hospedar ? maximo 6. '))
    mostrar_clientes(conn)
    id_cliente= int(input('digite o id do cliente : '))
    # processamento de dados tipo 1 
    if qtd_pessoas==1 and tipo ==1:
        preco_total = t1_1*qtd_dias
        print('o valor a ser pago é ',preco_total,' sua hospedagem é do tipo 1')
    elif qtd_pessoas == 2 and tipo ==1:
        preco_total = t1_2*qtd_dias
        print('o valor a ser pago é ',preco_total,'sua hospedagem de do tipo 1')
    elif qtd_pessoas ==3 and tipo ==1:
        preco_total=t1_3*qtd_dias
        print('o valor a ser pago é ',preco_total,'sua hospedagem de do tipo 1')
    elif qtd_pessoas == 4 and tipo ==1:
        preco_total=t1_4*qtd_dias
        print('o valor a ser pago é ',preco_total,'sua hospedagem de do tipo 1')
    elif qtd_pessoas == 5 and tipo == 1 :
        preco_total= t1_5*qtd_dias
        print('o valor a ser pago é ',preco_total,'sua hospedagem de do tipo 1')
    elif qtd_pessoas == 6 and tipo ==1:
        preco_total=t1_6*qtd_dias
        print('o valor a ser pago é ',preco_total,'sua hospedagem de do tipo 1')

        # adicionar reserva ao banco de dados 
    


    # processamento do tipo 2
    elif qtd_pessoas ==1 and tipo ==2:
        preco_total=t2_1*qtd_dias
        print('o valor a ser pago é ',preco_total,'sua hospedagem é do tipo 2 ')
    elif qtd_pessoas ==2 and tipo ==2:
        preco_total= t2_2*qtd_dias
        print('o valor a ser pago é ',preco_total,'sua hospedagem é do tipo 2 ')
    elif qtd_pessoas ==3 and tipo == 2:
        preco_total= t2_3*qtd_dias
        print('o valor a ser pago é ', preco_total,'sua hospedagem é do tipo 2 ')
    elif qtd_pessoas ==4 and tipo ==2:
        preco_total=t2_4*qtd_dias
        print('o valor a ser pago é ',preco_total,'sua hospedagem é do tipo 2 ')
    elif qtd_pessoas ==5 and tipo ==2:
        preco_total=t2_5*qtd_dias
        print('o valor a ser pago é ',preco_total,'sua hospedagem é do tipo 2 ')
    elif qtd_pessoas ==6 and tipo ==2:
        preco_total = t2_6*qtd_dias
        print('o valor a ser pago é ',preco_total,'sua hospedagem é do tipo 2 ')
        
        

        #ADICIONAR SQL
    sql =' INSERT INTO reservas (qtd_dia, qtd_pessoas, id_cliente , tipo, preco_total) values (?,?,?,?,?)' 

    valores_tipo = [qtd_dias, qtd_pessoas ,1, tipo , preco_total ]
    
    cursor.execute(sql,valores_tipo)
    
    conn.commit()
 # mostrar clientes
def mostrar_clientes(conn):
    cursor = conn.cursor()
    sql ='SELECT * FROM cliente' 
    dados=cursor.execute(sql)
    print('Clientes cadastrados :')
    for dado in dados :
        
        print(f'nome:{dado[1]},',f'cpf:{dado[3]}',f'email:{dado[4]}')
        

def mostrar_reservas(conn):
    cursor = conn.cursor()
    sql ='SELECT * FROM reservas' 
    dados=cursor.execute(sql)
    print('-------------------------')
    for dado in dados :
        
        print(f'ID cliente:{dado[1]}',f'qunatidade de dias:{dado[2]},',f'tipo:{dado[4]},',f'preços:{dado[5]}')
