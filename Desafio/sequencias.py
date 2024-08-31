def gera_sequencia(n):
    """Gera uma sequência de números de 0 até n-1.

    Args:
        n: O número limite da sequência (não incluído na lista).

    Returns:
        Uma lista contendo a sequência.

    Raises:
        ValueError: Se n for menor que 0.
        TypeError: Se n não for um número inteiro.
    """
    if not isinstance(n, int):
        raise TypeError("O argumento deve ser um número inteiro.")
    if n < 0:
        raise ValueError("O número deve ser maior ou igual a zero.")
    return list(range(n))

def sequencia_aritmetica(inicio, fim, passo=1):
    """Gera uma sequência aritmética.

    Args:
        inicio: O primeiro termo da sequência.
        fim: O último termo da sequência.
        passo: A razão da progressão aritmética.

    Returns:
        Uma lista com os termos da sequência.

    Raises:
        ValueError: Se fim for menor que inicio.
        TypeError: Se algum argumento não for um número inteiro.
    """
    if not all(isinstance(i, int) for i in [inicio, fim, passo]):
        raise TypeError("Todos os argumentos devem ser inteiros.")
    if fim < inicio:
        raise ValueError("O fim da sequência deve ser maior ou igual ao início.")

    sequencia = []
    valor = inicio
    while valor <= fim:
        sequencia.append(valor)
        valor += passo
    return sequencia
