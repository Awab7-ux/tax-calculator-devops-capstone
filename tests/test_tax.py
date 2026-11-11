import pytest

from tax import calculate_tax


@pytest.mark.parametrize(
    ("status", "income", "expected"),
    [
        ("single", 0, 0),
        ("single", 11000, 1100),
        ("single", 11001, 1100.12),
        ("single", 44725, 5147),
        ("single", 44726, 5147.22),
        ("single", 95375, 16290),
        ("single", 95376, 16290.24),
        ("single", 182100, 37104),
        ("single", 182101, 37104.32),
        ("married", 0, 0),
        ("married", 22000, 2200),
        ("married", 22001, 2200.12),
        ("married", 89450, 10294),
        ("married", 89451, 10294.22),
        ("married", 190750, 32580),
        ("married", 190751, 32580.24),
        ("married", 364200, 74208),
        ("married", 364201, 74208.32),
    ],
)
def test_tax_bracket_boundaries(status, income, expected):
    assert calculate_tax(income, status) == pytest.approx(expected)


@pytest.mark.parametrize("income", [-1, "not-a-number", None, float("nan")])
def test_invalid_income_raises(income):
    with pytest.raises(ValueError):
        calculate_tax(income, "single")


@pytest.mark.parametrize("status", ["head-of-household", None, [], 1])
def test_invalid_status_raises(status):
    with pytest.raises(ValueError):
        calculate_tax(50000, status)
