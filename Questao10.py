''' Crie um grafo vazio. Peça para o usuário digitar os vértices e as arestas desse grafo. 
O usuário deve informar os pares de vértices que formam cada aresta.
 Em seguida, peça para o usuário escolher uma das arestas e removê-la do grafo.
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
    
a, b = input('Qual das arestas voce deseja remover? ').split()

if a in grafo and b in grafo:
    grafo[a].remove(b)
    grafo[b].remove(a)
    print('A aresta foi removida!')
    print('O grafo atualizado: ', grafo)
else:
    print('Essa aresta nao existe!')


