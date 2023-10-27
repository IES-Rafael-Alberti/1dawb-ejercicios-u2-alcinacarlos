from src.ej2_03 import division
import pytest
@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
    (1, 0, "No se puede dividir entre cero."),
    (8, 4, "El resultado de la división es: 2.0"),
    (3, 3, "El resultado de la división es: 1.0"),
    (100, 2, "El resultado de la división es: 50.0")
    ]
)
def test(input_n1, input_n2, expected):
    assert division(input_n1, input_n2) == expected