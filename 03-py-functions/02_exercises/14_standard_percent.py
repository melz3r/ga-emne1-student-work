def calculate_tip(amount, tip_percent = 0):
    tip = amount * tip_percent / 100
    total = amount + tip
    return total

print(calculate_tip(100))
print(calculate_tip(100, 10))
print(calculate_tip(100, 30))