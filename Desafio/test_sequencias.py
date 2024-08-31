import pytest
from sequencias import gera_sequencia

def test_sequencia_de_cinco_numeros():
    assert gera_sequencia(5) == [0, 1, 2, 3, 4]

def test_sequencia_vazia():
    assert gera_sequencia(0) == []

def test_sequencia_numero_negativo():
    with pytest.raises(ValueError):
        gera_sequencia(-1)

def test_sequencia_numero_grande():
    assert gera_sequencia(1000)  # Ajuste o valor conforme a sua implementação

def test_sequencia_numero_nao_inteiro():
    with pytest.raises(TypeError):
        gera_sequencia(3.14)

def test_sequencia_string():
    with pytest.raises(TypeError):
        gera_sequencia("cinco")