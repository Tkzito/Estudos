#Declarar variaveis
#Node Nd
#inteiro posição
#inteiro cont
#Node Ndnovo
#Node temp
#Atribuir valor inicial
#cont = 0
#Nd = lista.proximo
#NdNovo.dado = 5
#posição = 10
#Percorrer listaaté encontrar o elemento nulom logo final da lista enquanto Nd deferente nulo
#enquanto lista.proximo diferente nulo
#Se a contador encontrar-se na posição desejada realizar a inserção do nodo
#se cont igual a posição
#temp = lista.proximo
#Ndnovo.proximo= temp
#fim se
#fim enquanto

def inserir (sel, item, pos):
    atual = self.inicio
    pos_atual = 0

    while atual.proximo != None:

        if pos_atual == (pos-1):
            pointer = atual
            node = Nodo (item)
            node.proximo = pointer.proximo
            pointer.proximo = node

        else:
            atual = atual.proximo
    pos_atual = pos_atual + 1

#Método 2

lista = [1, 2, 3, 4]
lista.insert(2, 10)
print(lista)