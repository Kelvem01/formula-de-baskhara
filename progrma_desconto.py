'''
Elabore um programa em Python que calcule o que deve ser pago por um produto,
 considerando o preço normal de etiqueta e a escolha da condição de pagamento.
 Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.

Código            Condição de pagamento

1                      À vista em dinheiro ou pix, recebe 15% de desconto

2                      À vista no cartão de crédito, recebe 10% de desconto

3                      Em duas vezes, preço normal de etiqueta mais juros de 5% (duas prestações iguais preço final dividido por 2)

4                      Em três vezes, preço normal de etiqueta mais juros de 10% ( 3 prestações iguais, preço final dividido por 3)



 Apresente todas as informações necessárias para que o usuário entende as condições de pagamento.

'''


d1 = 0.15*100
d2 = 0.10*100
d3 = 0.05*100
d4 = 0.10*100



print('''
1  À vista em dinheiro ou pix, recebe 15% de desconto

2  À vista no cartão de crédito, recebe 10% de desconto

3  Em duas vezes, preço normal de etiqueta mais juros de 5% (duas prestações iguais preço final dividido por 2)

4  Em três vezes, preço normal de etiqueta mais juros de 10% ( 3 prestações iguais, preço final dividido por 3)



''')
prod = float(input('digite o valor do produto : '))
pag = int(input('digite a forma de pagamento : '))

if pag ==1:
    valor = prod - d1 
    print(valor )