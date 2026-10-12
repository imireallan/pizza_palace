# Price matrix (per spec)
import math

SIZE_PRICES = {
    "Small": 10.00,
    "Medium": 15.00,
    "Large": 20.00,
}
BASIC_TOPPING_PRICE = 1.00
DELUXE_TOPPING_PRICE = 2.00
BASIC_TOPPINGS = {"Cheese", "Pepperoni", "Ham", "Pineapple"}
DELUXE_TOPPINGS = {"Sausage", "Feta Cheese", "Tomatoes", "Olives"}
TAX_RATE = 0.05


def calculate_pizza_price(size, toppings):
    if size not in SIZE_PRICES:
        raise ValueError(f"Unknown size: {size}")
    base = SIZE_PRICES[size]
    extra = 0.0
    for t in toppings:
        if t in DELUXE_TOPPINGS:
            extra += DELUXE_TOPPING_PRICE
        elif t in BASIC_TOPPINGS:
            extra += BASIC_TOPPING_PRICE
        else:
            raise ValueError(f"Unknown topping: {t}")
    return round(base + extra, 2)


def calculate_subtotal(pizzas):
    return sum(p["price"] for p in pizzas)


def calculate_tax(subtotal):
    return math.ceil(subtotal * TAX_RATE * 100) / 100


def calculate_receipt(pizzas):
    """Public API aligned with spec: takes pizza descriptions, returns receipt string."""
    priced = []
    for p in pizzas:
        price = calculate_pizza_price(p["size"], p.get("toppings", []))
        priced.append({"size": p["size"], "toppings": p.get("toppings", []), "price": price})
    return receipt_text(priced)


def receipt_text(order_items):
    lines = []
    subtotal = 0.0
    for item in order_items:
        lines.append(f"{item['size']} Pizza - {', '.join(item['toppings']) or 'No toppings'}: {item['price']:.2f}")
        subtotal += item["price"]
    tax = calculate_tax(subtotal)
    total = subtotal + tax
    lines.append(f"Subtotal: {subtotal:.2f}")
    lines.append(f"TAX (5%): {tax:.2f}")
    lines.append(f"Total: {total:.2f}")
    return "\n".join(lines)
