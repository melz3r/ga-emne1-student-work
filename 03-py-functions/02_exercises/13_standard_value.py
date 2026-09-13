def show_price(price, currency = "NOK"):
    return f"{price} {currency}"

print(show_price(100))
print(show_price(100, "EUR"))