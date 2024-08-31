def obter_estado_lampada(pergunta):
    """Obtém o estado de uma lâmpada a partir da resposta do usuário.

    Args:
        pergunta (str): A pergunta a ser feita ao usuário.

    Returns:
        bool: True se a lâmpada estiver acesa, False caso contrário.

    Raises:
        ValueError: Se a resposta do usuário for inválida.
    """
    while True:
        try:
            resposta = input(pergunta).lower()
            if resposta == 'sim':
                return True
            elif resposta == 'não':
                return False
            else:
                raise ValueError("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
        except ValueError as e:
            print(e)