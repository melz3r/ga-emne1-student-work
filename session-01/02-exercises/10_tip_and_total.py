item = input("Skriv hvilken vare du skal kjøpe: ")
price = float(input("Skriv hva varen koster (kun tall): "))
tip = price * 0.15
total_price = price + tip

print(f"Prisen for 1 stk {item} er kr {price:.2f},-")
print(f"15% tips av kr {price:.2f} er kr {tip:.2f},-")
print(f"Totalkostnad er {total_price:.2f},-. ")