''' Crie uma lista vazia e peça para o usuário digitar 10 números. Em seguida, adicione esses números
à lista utilizando um loop for.
'''

numeros = []

for i in range(1,11):
    num = int(input('Informe os números: '))
    numeros.append(num)

print('A lista de numeros informada: ', numeros)