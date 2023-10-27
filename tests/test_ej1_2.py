from src.ej2_02 import ingresar_contraseña
import pytest
@pytest.mark.parametrize(
    "input_n1, expected",
    [
    ("contraseña", "Contraseña correcta"),
    ("CONTRASEÑA", "Contraseña correcta"),
    ("cOnTrAsEñA", "Contraseña correcta"),
    ("asfafas", "Contraseña incorrecta"),
    ("PnfAOFaf", "Contraseña incorrecta"),
    ("contraseña123", "Contraseña incorrecta")
    ]
)
def test_ingresar_contraseña_params(input_n1, expected):
    assert ingresar_contraseña(input_n1) == expected