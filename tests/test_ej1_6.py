from src.ej2_06 import grupo_corresponde
import pytest
@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
    ("Sapillo", "H", "A"),
    ("Alejandra", "H", "B"),
    ("Paco", "H", "A"),
    ("Lauren", "H", "B")
    ]
)
def test(input_n1, input_n2, expected):
    assert grupo_corresponde(input_n1, input_n2) == expected