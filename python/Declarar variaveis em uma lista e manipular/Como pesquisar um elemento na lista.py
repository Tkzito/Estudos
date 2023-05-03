#Declarar variaveis
#Variavel Node Nd 
#Variavel inteiro cont
#cariavel node NdReferencia
#atribuir valores iniciais 
#cont = 0
#Nd = lista.proxima
#NdReferencia.dado = 5
#Percorrer lista até encontrar o elemento nulo, logo final da lista
#enquanto Nd diferente nulo
#Quando achar o nodo co o conteúdo iguao ao nodo de referênci, é um nodo que estamos procurando e informamos a sua posição
#se Nd.dado igual a NDReferencia.dado
#imprime Cont
#fimm se
#cont = cont + 1
#Nd = lista.proximo
#fim enquanto

#Método 1 - função que retorna se achou um elemento em uma lista

def ExisteNodo(self, item):
    atual = self.inicio
    status = False
    while atual != Node and not status:
        if atual.inf()==item:
            status = True
        else:
            atual = atual.proxNodo()
            return status