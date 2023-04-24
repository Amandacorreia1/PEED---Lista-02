'''Peça para o usuário digitar 3 nomes e crie um tupla com esses nomes. Em seguida, peça para o usuário 
escolher um dos nomes e substituir esse nome por outro nome que que ele também deve digitar.
'''
names = ()
for i in range(1,4):
    nomes = str(input(f'Informe {i}º nome: '))
    names = names + (nomes,)

lista = list(names)

print(''' Qual nome voce deseja mudar? Escolha uma das opcoes abaixo:
          
          1 - Mudar o primeiro nome
          2 - Mudar o segundo nome
          3 - Mudar o terceiro nome

''')

opcao = int(input('Informe a opcao: '))

if opcao == 1:
    novoNome = input('Digite o novo nome: ')
    lista[0] = novoNome
elif opcao == 2:
    novoNome = input('Digite o novo nome: ')
    lista[1] = novoNome
elif opcao == 3:
    novoNome = input('Digite o novo nome: ')
    lista[2] = novoNome

tupla = tuple(lista)
print('Lista de nome atualizada: ', tupla)


