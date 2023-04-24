'''Peça para o usuário digitar 5 números e crie uma lista com esses números. Em seguida, peça para o usuário mais um número 
e adicione esse número à lista 
''' 

numero = []

for i in range(1, 6):
    num = int(input('Informe os números: '))
    numero.append(num)

numA = int(input('Digite outro numero: '))
numero.append(numA)

print('Lista de numeros: ', numero)