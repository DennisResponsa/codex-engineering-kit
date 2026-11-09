"""Intentionally faulty teaching fixture. Do not use as an application module."""
from app import quote as validated_quote


def quote(items: list[tuple[int, int]], shipping_cents: int, discount_percent: int) -> int:
    # Reuse validation; the deliberate defect is only the discount base below.
    validated_quote(items, shipping_cents, discount_percent)
    subtotal = sum(price * quantity for price, quantity in items)
    return ((subtotal + shipping_cents) * (100 - discount_percent) + 50) // 100
