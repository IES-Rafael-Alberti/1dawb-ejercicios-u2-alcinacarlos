from src.ej22_11 import alreves_una_a_una
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    ("hola", "a\nl\no\nh\n"),
    ("testeando", "o\nd\nn\na\ne\nt\ns\ne\nt\n"),
    ("pytest", "t\ns\ne\nt\ny\np\n"),
    ("ayuda", "a\nd\nu\ny\na\n")
    ]
)
def test(input_n1, expected):
    assert alreves_una_a_una(input_n1) == expected