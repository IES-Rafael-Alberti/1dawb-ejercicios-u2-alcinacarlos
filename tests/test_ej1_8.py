from src.ej2_08 import leer_puntuacion
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (0.4, ("Aceptable", 960.0)),
    (0.0, ("Inaceptable", 0.0)),
    (0.6, ("Meritorio", 1440.0)),
    (0.8, ("Meritorio", 1920.0))
    ]
)
def test(input_n1, expected):
    assert leer_puntuacion(input_n1) == expected