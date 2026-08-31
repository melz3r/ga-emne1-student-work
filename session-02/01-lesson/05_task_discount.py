price = float(input("Oppgi kjøpsbeløp: "))

if price >= 1000:
    discount = 0.20
elif price >= 500:
    discount = 0.10
else:
    discount = 0
discounted_price = price * (1 - discount)
print(f"Final amount: {discounted_price:.2f}")