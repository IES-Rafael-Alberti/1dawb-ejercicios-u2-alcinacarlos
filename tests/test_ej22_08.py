from src.ej22_08 import triangulo
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (3, "1 \n3 1 \n5 3 1 \n"),
    (5, "1 \n3 1 \n5 3 1 \n7 5 3 1 \n9 7 5 3 1 \n"),
    (2, "1 \n3 1 \n"),
    (4, "1 \n3 1 \n5 3 1 \n7 5 3 1 \n")
    ]
)
def test(input_n1, expected):
    assert triangulo(input_n1) == expected