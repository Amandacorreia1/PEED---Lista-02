'''Peça para o usuário digitar 5 números e crie um conjunto com esses números.
Em seguida, verifique quantos elementos estão no conjunto.
'''
conjunto = set()
for i in range(1, 6):
    num = int(input(f'Digite o {i}º numero: '))
    conjunto.add(num)

quantidadeNumeros = len(conjunto)

print(f'O conjunto tem {quantidadeNumeros} numeros.')
        
    