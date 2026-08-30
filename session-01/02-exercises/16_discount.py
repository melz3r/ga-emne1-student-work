product_name = input("Skriv inn produkt: ")
unit_price = float(input("Enhetspris: "))
quantity = int(input("Antall enheter: "))
discount_percentage = float(input("Rabatt i prosent: "))

total_price_no_discount = unit_price * quantity
discount = total_price_no_discount / 100 * discount_percentage

total_price_with_discount = total_price_no_discount - discount

print(f"""Du har kjøpt {quantity} stk {product_name}
til kr {unit_price:.2f} pr stk med en rabatt på {discount_percentage:.1f} %.
Totalpris inkl. rabatt: kr {total_price_with_discount:.2f}.
""")
