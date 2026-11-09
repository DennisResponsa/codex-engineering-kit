"""Synthetic order totals. All amounts are integer cents; no tax calculation."""


def quote(items: list[tuple[int, int]], shipping_cents: int, discount_percent: int) -> int:
    """Discount merchandise only, round its net amount half-up, then add shipping."""
    if type(shipping_cents) is not int or shipping_cents < 0:
        raise ValueError('Shipping must be non-negative integer cents')
    if type(discount_percent) is not int or not 0 <= discount_percent <= 100:
        raise ValueError('Discount must be an integer from 0 to 100')
    if not items:
        raise ValueError('At least one item is required')
    subtotal = 0
    for price, quantity in items:
        if type(price) is not int or price < 0:
            raise ValueError('Prices must be non-negative integer cents')
        if type(quantity) is not int or quantity <= 0:
            raise ValueError('Quantities must be positive integers')
        subtotal += price * quantity
    return (subtotal * (100 - discount_percent) + 50) // 100 + shipping_cents
