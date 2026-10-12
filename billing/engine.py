# Price matrix (per spec)
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

import math

def calculate_pizza_price(size, toppings):
    base = SIZE_PRICES[size]
    extra = 0.0
    for t in toppings:
        if t in DELUXE_TOPPINGS:
            extra += DELUXE_TOPPING_PRICE
        elif t in BASIC_TOPPINGS:
            extra += BASIC_TOPPING_PRICE
        else:
            extra += BASIC_TOPPING_PRICE  # same price for unknown, or could raise
    return round(base + extra, 2)

def calculate_subtotal(pizzas):
    return sum(p["price"] for p in pizzas)

def calculate_tax(subtotal):
    return math.ceil(subtotal * TAX_RATE * 100) / 100

def receipt_text(order_items):
    lines = []
    for item in order_items:
        lines.append(f"{item['size']} Pizza - {', '.join(item['toppings']) or 'No toppings'}: {item['price']:.2f}")
    subtotal = sum(i["price"] for i in order_items)
    tax = calculate_tax(subtotal)
    total = subtotal + tax
    lines.append(f"Subtotal: {subtotal:.2f}")
    lines.append(f"TAX (5%): {tax:.2f}")
    lines.append(f"Total: {total:.2f}")
    return "\n".join(lines)
