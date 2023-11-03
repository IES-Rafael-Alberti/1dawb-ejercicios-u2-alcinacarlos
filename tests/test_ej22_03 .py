from src.ej22_03 import impares
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (10, "1, 3, 5, 7, 9"),
    (20, "1, 3, 5, 7, 9, 11, 13, 15, 17, 19"),
    (7, "1, 3, 5, 7"),
    (3, "1, 3"),
    (9, "1, 3, 5, 7, 9")
    ]
)
def test(input_n1, expected):
    assert impares(input_n1) == expected