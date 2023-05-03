#Declarar variaveis
#Node NdAnterior
#Node NdAtual
#Node NdExcluir
#inteiro posicao
#Atribuir valores iniciais
#Posição = 10
#NdAnterior = lista
#NdAtual= Lista.proximo
#Percorrer lista até encontrar o elemento nulo, logo final da lista enquanto Nd diferente nulo
#enquanto NdAtual.priximo diferente nulo
#Achou o elemento para excluir
#se NdAtual.proximo igual a NdExcluir
#NdAnterior.proximo = NdAtual.proximo
#Libera a memoria
#liberaMemoria(Ndatual)
#sair
#fim se
#Atualiza as variáveis atual e anterior para a próxima interação do laço
#NdAnterior = NdAtual
#NdAtual = Ndatual.proximo
#fim enquanto

#Método 1
def remover(sef,pos):
    atual = self.inicio
    pos_atual = 0

    while atual.proximo != None:

        if pos_atual == (pos-1):
            next = atual.proximo
        else:
            atual = atual.priximo

    pos_atual = pos_atual +1
#Método 2
lista = [1, 2, 3, 4]
lista.pop(2)
print(lista)