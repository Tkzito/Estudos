#Declarar variáveis
#variavel lista =[]
#verificar se a lista está vazia, caso positivo retornar 'true' se não False
#se (lista.proximo igual a nulo) então
#retorne true
#se não
#retorne false
#fim se
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
#Funçao que verifica a lista
def verifica_vazia(Lista):
     if Lista.cabeca == None :
          print('True')
     else:
          print('False')
#Codigo principal
Lista = ListaEncadeada()
verifica_vazia(Lista)
