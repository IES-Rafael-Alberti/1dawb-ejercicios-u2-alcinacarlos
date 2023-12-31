from src.ej22_04 import cuenta_atras
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (10, "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0"),
    (20, "20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0"),
    (7, "7, 6, 5, 4, 3, 2, 1, 0"),
    (3, "3, 2, 1, 0"),
    (9, "9, 8, 7, 6, 5, 4, 3, 2, 1, 0")
    ]
)
def test(input_n1, expected):
    assert cuenta_atras(input_n1) == expected