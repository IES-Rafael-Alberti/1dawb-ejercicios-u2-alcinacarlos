from src.ej2_09 import calcular_precio
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (10, 5),
    (3, 0),
    (5, 5),
    (54, 10)
    ]
)
def test(input_n1, expected):
    assert calcular_precio(input_n1) == expected