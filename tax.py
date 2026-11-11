"""Progressive tax estimates for the supported filing statuses."""

from math import isfinite


TAX_BRACKETS = {
    "single": ((11000, 0.10), (44725, 0.12), (95375, 0.22),
               (182100, 0.24), (float("inf"), 0.32)),
    "married": ((22000, 0.10), (89450, 0.12), (190750, 0.22),
                (364200, 0.24), (float("inf"), 0.32)),
}


def calculate_tax(income, status):
    """Return tax due for a non-negative income and supported filing status."""
    if not isinstance(status, str) or status not in TAX_BRACKETS:
        raise ValueError("status must be 'single' or 'married'")

    if isinstance(income, bool):
        raise ValueError("income must be a non-negative number")
    try:
        amount = float(income)
    except (OverflowError, TypeError, ValueError):
        raise ValueError("income must be a non-negative number") from None

    if not isfinite(amount) or amount < 0:
        raise ValueError("income must be a non-negative number")

    tax = 0.0
    lower_bound = 0.0
    for upper_bound, rate in TAX_BRACKETS[status]:
        taxable = min(amount, upper_bound) - lower_bound
        if taxable > 0:
            tax += taxable * rate
        if amount <= upper_bound:
            break
        lower_bound = upper_bound

    return round(tax, 2)
