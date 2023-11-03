from src.ej2_10 import formar_eleccion
import pytest
@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
    (1, ["Tomate", "Mozzarella", "Pimiento"], "Has elegido una pizza vegetariana con los siguientes ingredientes: Tomate, Mozzarella, Pimiento"),
    (2, ["Tomate", "Mozzarella", "Pepperoni"], "Has elegido una pizza NO vegetariana con los siguientes ingredientes: Tomate, Mozzarella, Pepperoni"),
    (1, ["Tomate", "Mozzarella", "Tofu"], "Has elegido una pizza vegetariana con los siguientes ingredientes: Tomate, Mozzarella, Tofu"),
    (2, ["Tomate", "Mozzarella", "Jamón"], "Has elegido una pizza NO vegetariana con los siguientes ingredientes: Tomate, Mozzarella, Jamón")
    ]
)
def test(input_n1, input_n2, expected):
    assert formar_eleccion(input_n1, input_n2) == expected