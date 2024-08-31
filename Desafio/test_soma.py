import pytest
from soma import soma

def test_soma_valores():
    assert soma(5) == 15
    assert soma(10) == 55

def test_soma_limite_negativo():
    with pytest.raises(ValueError):
        soma(-1)

def test_soma_limite_nao_inteiro():
    with pytest.raises(ValueError):
        soma(3.14)

def test_soma_limite_string():
    with pytest.raises(ValueError):
        soma("cinco")
