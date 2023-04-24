''' Peça para o usuário digitar 5 números e crie um conjunto com esses números.
 Em seguida, verifique se o número 3 está presente no conjunto.
 '''
conjunto = set()

for i in range(1,6):
    num = int(input('Informe os numeros: '))
    conjunto.add(num)
    
if 3 in conjunto:
    print('O numero 3 esta presente no conjunto.')
else: 
    print('O numero 3 nao esta presente no conjunto')