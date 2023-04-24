''' Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes.
 Em seguida, verifique quantas vezes o nome 'Maria' aparece na tupla.
 '''

names = []

for i in range(3):
    nome01 = input(f'Digite o {i+1}º nome: ')
    names.append(nome01)


nomes = tuple(names)

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
