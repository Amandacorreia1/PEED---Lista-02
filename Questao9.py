'''Peça para o usuário digitar 10 números e crie um conjunto com esses números. 
Em seguida, remova todos os números pares do conjunto.
'''

conjunto = set()
for i in range(1,11):
    numero = int(input(f'Digite o {i} numero: '))
    conjunto.add(numero)

pares = set()
for numero in conjunto:
    if numero % 2 == 0:
        pares.add(numero)

conjunto = conjunto - pares
print(conjunto)
 
    
