#Declarar uma variáveis do tipo nodo
#variavel Node Nd

#Atribuir um elemento na lista
#Nd = lista.proximo
#Realizar a impressão do nodo
#imprime Nd

#classe Nodo
class Nodo:
    def __init__(self, codigo=0, proximo_nodo=None):
        self.codigo = codigo
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.codigo, self.proximo)
#classe Lista Encadeada
class ListaEncadeada:

        def __init__(self):
            self.cabeca = None

        def __repr__(self):
            return "[" + str(self.cabeca) + "]"
#Codigo principal
Lista = ListaEncadeada()
Primeiro = Lista.cabeca
print(Primeiro)

