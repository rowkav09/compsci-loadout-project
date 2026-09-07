import pytest

from models.wear import wear_category


@pytest.mark.parametrize(
    "float_value, expected",
    [
        (0.00, "Factory New"),
        (0.069, "Factory New"),
        (0.07, "Minimal Wear"),
        (0.149, "Minimal Wear"),
        (0.15, "Field-Tested"),
        (0.379, "Field-Tested"),
        (0.38, "Well-Worn"),
        (0.449, "Well-Worn"),
        (0.45, "Battle-Scarred"),
        (1.00, "Battle-Scarred"),
    ],
)
def test_wear_category_boundaries(float_value, expected):
    assert wear_category(float_value) == expected
