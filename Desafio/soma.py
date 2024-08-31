def soma(limite):
    """Calcula a soma de todos os números de 0 até limite (inclusive).

    Args:
        limite: O número até o qual somar.

    Returns:
        A soma de todos os números de 0 até limite.
    """
    if not isinstance(limite, int) or limite < 0:
        raise ValueError("O limite deve ser um número inteiro não negativo.")
    
    total = 0
    for i in range(limite + 1):
        total += i
    return total

# Exemplo de uso:
if __name__ == "__main__":
    limite = int(input("Digite o limite superior: "))
    resultado = soma(limite)
    print(f"A soma dos números de 0 até {limite} é {resultado}.")
