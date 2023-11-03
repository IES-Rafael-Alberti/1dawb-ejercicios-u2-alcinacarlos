from src.ej22_05 import cuenta_atras
import pytest
@pytest.mark.parametrize(
    "input_n1, input_n2, input_n3, expected",
    [
    (1000, 3, 20, "Año 1: 1200.00 €\nAño 2: 1440.00 €\nAño 3: 1728.00 €\n"),
    (2000, 2, 10, "Año 1: 2200.00 €\nAño 2: 2420.00 €\n"),
    (2300, 4, 15,"Año 1: 2645.00 €\nAño 2: 3041.75 €\nAño 3: 3498.01 €\nAño 4: 4022.71 €\n")
    ]
)
def test(input_n1, input_n2, input_n3, expected):
    assert cuenta_atras(input_n1, input_n2 , input_n3) == expected