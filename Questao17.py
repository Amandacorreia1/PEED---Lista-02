''' Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes.
 Em seguida, verifique quantas vezes o nome 'Maria' aparece na tupla.
 '''
nome01 = input('Digite o primeiro nome: ')
nome02 = input('Digite o segundo nome: ')
nome03 = input('Digite o terceiro nome: ')

nomes = (nome01, nome02, nome03)

quantidadeMaria = 0


for n in range(len(nomes)):
    if nomes[n].lower() == 'maria':
        quantidadeMaria += 1

'''
for n in nomes:
    if n.lower() == 'maria':
        quantidadeMaria += 1
'''

print(f'O nome Maria aparece {quantidadeMaria} vezes na tupla.')