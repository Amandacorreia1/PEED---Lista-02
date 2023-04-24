'''Crie um dicionário vazio. Peça para o usuário digitar as chaves e os valores desse dicionário.
 Em seguida, adicione uma nova chave e valor ao dicionário, onde a chave é 
 'cidade' e o valor é a cidade em que o usuário nasceu.
 '''
dicionario = {}
print('Informe as chaves e valores desse dicionario')

for i in range(1,4):
    chave = input(f'Digite a {i}º chave: ')
    valor = input('Digite o valor da chave: ')
    dicionario[chave] = valor
    
dicionario['cidade'] = input('Digite a cidade em que voce nasceu: ')

print('O valor da chave "Cidade" eh: '  ,dicionario['cidade'])