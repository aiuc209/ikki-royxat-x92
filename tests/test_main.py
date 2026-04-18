import pytest

def power(base, exponent):
    return base ** exponent

def calculate_powers(asos, daraja):
    return [power(base, exponent) for base, exponent in zip(asos, daraja)]

@pytest.mark.parametrize("asos, daraja, expected", [
    ([1, 2, 3], [1, 2, 3], [1, 4, 27]),
    ([4, 5, 6], [2, 3, 4], [16, 125, 1296]),
    ([7, 8, 9], [1, 2, 3], [7, 64, 729]),
])
def test_calculate_powers(asos, daraja, expected):
    assert calculate_powers(asos, daraja) == expected
