'''Peça para o usuário digitar 5 números e crie uma tupla com esses números. Em seguida, 
retorne o primeiro elemento da tupla.
'''
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))
num4 = int(input('Digite o quarto numero: '))
num5 = int(input('Digite o quinto numero: '))

tupla = (num1 , num2, num3, num4, num5)

elementoUm = tupla[0]
print('O primeiro elemento da tupla é: ', elementoUm)
