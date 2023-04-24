''' Peça para o usuário digitar 10 números e crie uma lista com esses números. 
Em seguida, multiplique cada elemento da lista por 2 e crie uma nova lista com esses valores.
'''
numero = []
for i in range(1,11):
    num = int(input(f'digite o {i}º numero: '))
    numero.append(num)
    
numeroMultiplicado = []

for num in numero:
    multi = 2 * num
    numeroMultiplicado.append(multi)
    
print('Lista de numeros original: ', numero)   
print('O valor dos numeros digitados e multiplicados por dois: ', numeroMultiplicado)
