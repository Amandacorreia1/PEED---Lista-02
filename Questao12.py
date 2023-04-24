''' Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes.
 Em seguida, verifique se o nome 'Maria' está presente na tupla.
'''
nome01 = input('Digite o primeiro nome: ')
nome02 = input('Digite o segundo nome: ')
nome03 = input('Digite o terceiro nome: ')

tupla = (nome01, nome02, nome03)
print(tupla)

if 'Maria' in tupla or 'maria' in tupla:
    print('O nome Maria está na tupla.')
else:
    print('O nome Maria nao está na tupla.')
    