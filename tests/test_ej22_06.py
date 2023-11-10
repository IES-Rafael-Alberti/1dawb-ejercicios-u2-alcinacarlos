from src.ej22_06 import simbolos
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (3, "*\n**\n***\n"),
    (5, "*\n**\n***\n****\n*****\n"),
    (7, "*\n**\n***\n****\n*****\n******\n*******\n"),
    (4, "*\n**\n***\n****\n")
    ]
)
def test(input_n1, expected):
    assert simbolos(input_n1) == expected