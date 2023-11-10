from src.ej22_02 import años_cumplidos
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (3, "Has cumplido 1 años\nHas cumplido 2 años\nHas cumplido 3 años\n"),
    (5, "Has cumplido 1 años\nHas cumplido 2 años\nHas cumplido 3 años\nHas cumplido 4 años\nHas cumplido 5 años\n"),
    (4, "Has cumplido 1 años\nHas cumplido 2 años\nHas cumplido 3 años\nHas cumplido 4 años\n"),
    (2, "Has cumplido 1 años\nHas cumplido 2 años\n")
    ]
)
def test(input_n1, expected):
    assert años_cumplidos(input_n1) == expected