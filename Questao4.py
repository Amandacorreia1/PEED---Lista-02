''' Peça para o usuário digitar 5 números e crie um conjunto com esses números.
Em seguida, peça para o usuário escoher um dos números e removê-lo do conjunto
'''
conjunto = set()

for i in range(1,6):
    num = int(input('Informe os numeros: '))
    conjunto.add(num)

removerNum = int(input('Qual número voce deseja remover do conjunto de numeros digitados? '))
conjunto.discard(removerNum)

print('O conjunto de numeros atualizado eh: ', conjunto)
