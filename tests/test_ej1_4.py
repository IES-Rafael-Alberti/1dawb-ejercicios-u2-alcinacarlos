from src.ej2_04 import par_impar
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (1, "1 es impar."),
    (8, "8 es par."),
    (3, "3 es impar."),
    (100, "100 es par.")
    ]
)
def test(input_n1, expected):
    assert par_impar(input_n1) == expected