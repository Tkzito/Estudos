def acao(self,item):
    atual = self.inicio
    status = False
    while atual != None and not status:
        if atual.dado()==item:
            status = True
        else:
            atual = atual.prox()
        return status
    