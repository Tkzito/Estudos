import pytest
from interruptores import is_interruptor  # Importação corrigida

@pytest.mark.parametrize("estado, resultado_esperado", [
    (True, "Ligado"),
    (False, "Desligado"),
    (None, "Estado inválido"),
    (1, "Estado inválido"),
    (0, "Estado inválido")
])
def test_interruptor(estado, resultado_esperado):
    if resultado_esperado == "Estado inválido":
        with pytest.raises(ValueError):
            is_interruptor(estado)
    else:
        assert is_interruptor(estado) == resultado_esperado
