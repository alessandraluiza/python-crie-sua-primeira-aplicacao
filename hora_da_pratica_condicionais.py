#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
numero = int(input('Informe um número:'))

if numero % 2 == 0:
    print('O número é par')
else:
    print('O número é impar')

#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo 
# com as seguintes condições:
#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.

idade = int(input('Informe sua idade: '))

if idade >= 0 and idade <= 12:
    print ('Você é uma criança.')
elif idade >= 13 and idade <= 18:
    print ('Você é um adolescente.')
else:
    print ('Você é um adulto.')

#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a 
# senha fornecidos correspondem aos valores esperados determinados por você.

usuario_informado = input('Informe o seu usuario: ')
senha_informada = input('Informe a sua senha: ')

usuario_esperado = 'bolinha'
senha_esperada = '4523'


if usuario_informado == usuario_esperado and senha_informada == senha_esperada:
    print ('Você esta logado')
else:
    print('Usuário ou senha incorreto')


#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano 
# cartesiano o ponto se encontra de acordo com as seguintes condições:

#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.

coord_x_informada = float(input('Informe a coordenada x: '))
coord_y_informada = float(input('Informe a coordenada y: '))

if coord_x_informada > 0 and coord_y_informada > 0:
    print('Primeiro quadrante')
elif coord_x_informada < 0 and coord_y_informada > 0:
    print('Segundo quadrante')
elif coord_x_informada < 0 and coord_y_informada < 0:
    print('Terceiro quadrante')
elif coord_x_informada > 0 and coord_y_informada < 0:
    print('Quarto quadrante')