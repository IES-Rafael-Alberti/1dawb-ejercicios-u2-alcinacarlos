from src.ej2_05 import tributar
import pytest
@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
    (18, 1000, "Debes tributar"),
    (24, 40000, "Debes tributar"),
    (18, 100, "No debes tributar"),
    (3, 20000, "No debes tributar")
    ]
)
def test(input_n1, input_n2, expected):
    assert tributar(input_n1, input_n2) == expected