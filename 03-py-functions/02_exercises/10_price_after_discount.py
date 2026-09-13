def calculate_discounted_price(price, discount_percent):
    discount = price * discount_percent / 100
    total_price = price - discount
    return total_price

result = calculate_discounted_price(1000, 25)

print(f"Totalsum etter rabatt: kr {result:.2f}")

