total = 0

for number in range(1, 11):
    print(f"Behandler {number}:")
    total += number
    print(f"Foreløpig sum: {total}")
print(f"Den endelige summen er: {total}")