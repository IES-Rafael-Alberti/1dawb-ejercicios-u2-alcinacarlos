from src.ej2_07 import tipo_impositivo
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    (1000, "5%"),
    (19000, "15%"),
    (34000, "20%"),
    (67437347347, "45%")
    ]
)
def test(input_n1, expected):
    assert tipo_impositivo(input_n1) == expected