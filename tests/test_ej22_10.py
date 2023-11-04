from src.ej22_10 import es_primo
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (2, "Es primo"),
    (97, "Es primo"),
    (4, "No es primo"),
    (3163, "Es primo")
    ]
)
def test(input_n1, expected):
    assert es_primo(input_n1) == expected