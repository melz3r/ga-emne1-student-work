number_limit = int(input("Skriv inn et heltall: "))

number = 1
print(f"Dette er kvadrattallene innen grensen som er {number_limit}:")
while number ** 2 <= number_limit:
    print(number ** 2)
    number += 1