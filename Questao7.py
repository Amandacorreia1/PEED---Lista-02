'''Peça para o usuário digitar 5 números e crie uma tupla com esses números. Em seguida, 
retorne o primeiro elemento da tupla.
'''

numeros = []

for i in range(5):

    num = int(input('Digite o primeiro numero: '))
    numeros.append(num)

tupla = tuple(numeros)

elementoUm = tupla[0]
print('O primeiro elemento da tupla é: ', elementoUm)
