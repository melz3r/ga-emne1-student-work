product_name = input("Produktnavn: ")
unit_price = float(input("Enhetspris: "))
quantity = int(input("Antall: "))
tax_rate = 0.25

total_price = unit_price * quantity
tax = total_price * tax_rate
price_with_tax = total_price + tax

print(f"""
Bekrefter følgende bestilling:

{quantity} stk {product_name} à kr {unit_price:.2f}
Totalpris eks mva: kr {total_price:.2f}
Mva: kr {tax:.2f}
Totalpris inkl mva: kr {price_with_tax:.2f}
""")