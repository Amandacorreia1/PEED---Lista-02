''' Crie uma lista vazia e peça para o usuário digitar 10 números.
 Em seguida, retorne os elementos de índice par da lista.
 '''
numeros = []

for i in range(1,11):
    num = int(input(f'Informe o {i}º numero: '))
    numeros.append(num)
    
print('Os numeros que possui indice par da lista:')
for i in range(0, len(numeros), 2):
    
    print(numeros[i])
