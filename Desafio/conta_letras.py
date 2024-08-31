import os
from unidecode import unidecode

def contar_as(texto):
    """Conta o número de vezes que a letra 'a' aparece em um texto."""
    if isinstance(texto, str) and texto.endswith('.txt'):
        caminho_arquivo = os.path.abspath(texto)
        if not os.path.isfile(caminho_arquivo):
            print(f"Arquivo '{caminho_arquivo}' não encontrado.")
            return 0
        
        try:
            with open(caminho_arquivo, 'r') as file:
                texto = file.read()
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo: {e}")
            return 0
    elif not isinstance(texto, str):
        raise TypeError("O argumento deve ser uma string.")
    
    texto_sem_acento = unidecode(texto).lower()
    print(f"Texto processado: {texto_sem_acento}")
    contagem_a = texto_sem_acento.count('a')
    print(f"Contagem de 'a': {contagem_a}")
    return contagem_a
