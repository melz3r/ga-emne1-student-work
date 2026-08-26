item = input("Skriv hvilken vare du skal selge: ")
price = float(input("Skriv hva varen koster uten mva (kun tall): "))
tax = price * 0.15
total_price = price + tax

print(f"Prisen for 1 stk {item} er kr {price:.2f},- pluss kr {tax:.2f},- i mva, altså totalt kr {total_price:.2f},-. ")