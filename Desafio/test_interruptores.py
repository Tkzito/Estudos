import random

def obter_resposta(pergunta):
    while True:
        try:
            resposta = input(pergunta).lower()
            if resposta in ['sim', 'não']:
                return True if resposta == 'sim' else False
            else:
                raise ValueError("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
        except ValueError as e:
            print(e)

def resolver_enigma(num_lampadas):
    """Resolve o enigma dos interruptores.

    Args:
        num_lampadas (int): Número de lâmpadas.

    Returns:
        dict: Dicionário com a correspondência entre interruptores e lâmpadas.
    """

    # Cria uma lista aleatória para representar a correspondência
    correspondencia = list(range(1, num_lampadas + 1))
    random.shuffle(correspondencia)

    # Simula a interação com os interruptores e lâmpadas
    # ... (implementação da lógica do enigma)

    return dict(zip(range(1, num_lampadas + 1), correspondencia))

def test_resolver_enigma(mocker):
    # Testes com diferentes números de lâmpadas
    for num_lampadas in range(2, 5):
        mock_input = mocker.patch('builtins.input')
        # ... (configurar as respostas de acordo com a lógica do enigma)
        resultado = resolver_enigma(num_lampadas)
        # ... (verificar se o resultado está correto)

    # Testes com entradas inválidas
    # ...

if __name__ == "__main__":
    num_lampadas = int(input("Digite o número de lâmpadas: "))
    resultado = resolver_enigma(num_lampadas)
    print("A correspondência entre interruptores e lâmpadas é:", resultado)