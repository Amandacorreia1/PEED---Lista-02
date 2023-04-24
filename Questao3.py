'''crie um dicionário vazio. Peça para o usuário digitar uma chave e um valor e adicione 
esses dados ao dicionário. Em seguida, peça para o usuário adicionar mais uma chave e um valor
e adicione esses dados ao dicionário também
'''

dicionário = {}
chave01 = input('Digite uma chave: ')
valor01 = input('Digite um valor: ')

dicionário[chave01] = valor01

chave02 = input('Digite mais uma chave: ')
valor02 = input('Digite mais um valor: ')

dicionário[chave02] = valor02

print(dicionário)