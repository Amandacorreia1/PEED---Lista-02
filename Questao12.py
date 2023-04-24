''' Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes.
 Em seguida, verifique se o nome 'Maria' está presente na tupla.
'''

name = []

for i in range(3):

    nome01 = input(f'Digite o {i+1}º nome: ')
    name.append(nome01)

tupla = tuple(name)
print(tupla)

if 'Maria' in tupla or 'maria' in tupla:
    print('O nome Maria está na tupla.')
else:
    print('O nome Maria nao está na tupla.')
    