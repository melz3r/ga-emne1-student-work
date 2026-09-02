weight = float(input("Vekt i kg: "))

if weight <= 2:
    price = 79
elif weight <= 5:
    price = 129
elif weight <= 10:
    price = 199
else:
    price = None
    print("Varen er for tung.")

# None: Variabelen eksisterer, men den har ikke fått verdi enda.

if price is not None:
    print (f"Varen koster kr {price:.2f}")
