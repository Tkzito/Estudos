def is_interruptor(estado):
    """Verifica o estado do interruptor e retorna a string correspondente.
    
    Args:
        estado: Pode ser True (ligado), False (desligado) ou None/qualquer outro valor inválido.
    
    Returns:
        Uma string representando o estado do interruptor.
    
    Raises:
        ValueError: Se o estado for inválido.
    """
    if estado is True:
        return "Ligado"
    elif estado is False:
        return "Desligado"
    else:
        raise ValueError("Estado inválido")
