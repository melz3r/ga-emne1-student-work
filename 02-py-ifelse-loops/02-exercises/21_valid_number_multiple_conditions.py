count = 0

for number in range(1, 101):
    if number % 3 == 0 and 20 < number < 80:
        print(number)
        count += 1
print(f"Antall tall i tallrekken: {count}")

