'''Crie um grafo vazio. Peça para o usuário digitar os vértices e as arestas desse grafo.
 O usuário deve informar os pares de vértices que formam cada aresta.
  Em seguida, verifique se a aresta ('A', 'C') está presente no grafo.
  '''
grafo = {}

num_vertices = int(input('Digite o numero de vértices do grafo: '))
for i in range(num_vertices):
    vertice = input('Digite o nome do vértice: ')
    grafo[vertice] = []
    
num_arestas = int(input('Digite o número de arestas do grafo: '))
for i in range(num_arestas):
    a, b = input(f'Digite os vértices que formam a aresta {i+1}: ').split()
    grafo[a].append(b)
    grafo[b].append(a)
    
if 'A' in grafo['C']:
    print('A Aresta ("A", "C") esta presente no grafo!')

else:
    print('A Aresta ("A", "C") nao esta presente no grafo!')
