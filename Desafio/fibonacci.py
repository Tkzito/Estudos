def encontrar_termos_mais_proximos(n):
    """Encontra os dois termos da sequência de Fibonacci mais próximos de n."""
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a, b

def is_fibonacci(n):
    """Verifica se um número pertence à sequência de Fibonacci."""
    if n < 0:
        raise ValueError("Número negativo não é permitido.")
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

def verificar_sequencia_fibonacci(numeros):
    """Verifica se os números em uma lista pertencem à sequência de Fibonacci."""
    resultados = []
    for numero in numeros:
        if numero < 0:
            resultado = f"O número {numero} é negativo. A sequência de Fibonacci contém apenas números naturais."
        else:
            if is_fibonacci(numero):
                resultado = f"O número {numero} pertence à sequência de Fibonacci."
            else:
                a, b = encontrar_termos_mais_proximos(numero)
                resultado = f"O número {numero} não pertence à sequência de Fibonacci. Os termos mais próximos são {a} e {b}."
        resultados.append(resultado)
    return resultados

def main():
    # Solicita a entrada do usuário
    numeros_str = input("Informe uma lista de números inteiros separados por vírgulas: ")
    numeros = [int(num) for num in numeros_str.split(',') if num.isdigit()]

    # Chama a função para verificar a sequência e exibe os resultados
    resultados = verificar_sequencia_fibonacci(numeros)
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()
