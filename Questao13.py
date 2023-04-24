''' Crie um dicionário vazio. Peça para o usuário digitar as chaves e os valores desse dicionário.
 Em seguida, verifique se a chave 'profissão' está presente no dicionário.
 '''
dicionario = {}

for i in range(1, 4):
    chave = input('Informe a chave: ')
    valor = input('informe o valor: ')
    
    dicionario[chave] = valor
    
if 'profissão' in dicionario:
    print('A chave profissão esta presente no dicionario')
    
else: 
    print('A chave profissão não esta presente no dicionario')
    
    