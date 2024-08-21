#1 - Crie uma lista para cada informação a seguir:
#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Maria', 'João', 'Benedita', 'Francisca']
anos = [1996,2024]

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    print(numero)
print("-----------")

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

for numero in numeros:
    if numero % 2 == 1:
        soma = soma + numero
print(soma)

print("-----------")

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

for i in range (10, 0, -1):
    print(i)

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero = int(input('Informe um número: '))
for i in range(1,11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')

#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
# Utilize um bloco try-except para lidar com possíveis exceções.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

try:
    for numero in numeros:
        soma += numero
    print(soma)
except Exception as e:
    print(f'Ocorreu um erro: {e}')

#7 - Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

try:
    for numero in numeros:
        soma += numero
    media = soma / len(numeros)
    print(f'Média dos valores: {media}')
except ZeroDivisionError:
    print('A lista está vazia, não é possível calcular a média.')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
