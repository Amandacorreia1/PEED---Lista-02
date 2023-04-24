'''Crie um dicionário vazio. Peça para o usuário digitar as chaves e os valores dessse dicionário. 
Em seguida, retorne o valor da chave 'idade'.
'''
dicionario = {}

qntd = int(input('Quantas chaves e valores voce deseja digitar? '))

for i in range(qntd):
    chave = input('Informe a chave: ')
    valor = input('Informe o valor: ')
    
    dicionario[chave] = valor

if 'idade' in dicionario:
    print('O valor da idade informada é: ', dicionario['idade'])

else: 
    print('Não foi encontrado a chave idade.')
