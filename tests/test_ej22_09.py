from src.ej22_09 import verificar_contraseña
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    ("agsgagasg", False),
    ("COntraseña", False),
    ("contraseña", "Contraseña Correcta"),
    ("holasxafasf", False)
    ]
)
def test(input_n1, expected):
    assert verificar_contraseña(input_n1) == expected