import pytest
from fibonacci import is_fibonacci, verificar_sequencia_fibonacci

# Dados de teste para is_fibonacci
test_data = [
    (0, True), 
    (1, True), 
    (6, False), 
    (8, True), 
    (-1, ValueError)
]

@pytest.mark.parametrize("number, expected", test_data)
def test_fibonacci_with_data(number, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            is_fibonacci(number)
    else:
        assert is_fibonacci(number) == expected

# Testando a função verificar_sequencia_fibonacci
def test_verificar_sequencia_fibonacci():
    numeros = [0, 1, 6, 8, -1]
    resultados = verificar_sequencia_fibonacci(numeros)
    assert resultados[0] == "O número 0 pertence à sequência de Fibonacci."
    assert resultados[1] == "O número 1 pertence à sequência de Fibonacci."
    assert resultados[2] == "O número 6 não pertence à sequência de Fibonacci. Os termos mais próximos são 5 e 8."
    assert resultados[3] == "O número 8 pertence à sequência de Fibonacci."
    assert resultados[4] == "O número -1 é negativo. A sequência de Fibonacci contém apenas números naturais."
