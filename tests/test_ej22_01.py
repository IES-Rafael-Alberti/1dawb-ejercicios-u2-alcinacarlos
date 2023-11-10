from src.ej22_01 import imprimir_10
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    ("hola", "hola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\n"),
    ("algo", "algo\nalgo\nalgo\nalgo\nalgo\nalgo\nalgo\nalgo\nalgo\nalgo\n"),
    ("helloxd", "helloxd\nhelloxd\nhelloxd\nhelloxd\nhelloxd\nhelloxd\nhelloxd\nhelloxd\nhelloxd\nhelloxd\n"),
    ("prueba", "prueba\nprueba\nprueba\nprueba\nprueba\nprueba\nprueba\nprueba\nprueba\nprueba\n"),
    ("testeando", "testeando\ntesteando\ntesteando\ntesteando\ntesteando\ntesteando\ntesteando\ntesteando\ntesteando\ntesteando\n")
    ]
)
def test(input_n1, expected):
    assert imprimir_10(input_n1) == expected