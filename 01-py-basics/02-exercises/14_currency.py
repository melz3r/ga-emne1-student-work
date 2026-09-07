def convert_currency(nok_amount, exchange_rate):
    return nok_amount * exchange_rate

amount = float(input("Skriv inn et beløp i NOK: "))
rate = float(input("Skriv inn valutakursen (hvor mye 1 NOK er verdt i målvalutaen): "))

result = convert_currency(amount, rate)

print(f"Resultat: {result:.2f} NOK")
print("Test 1: 100 NOK med kurs 1")
print(convert_currency(100, 1))
print("Test 2: 500 NOK med kurs 0.12")
print(convert_currency(500, 0.12))
print("Test 3: 1000 NOK med kurs 0.08")
print(convert_currency(1000, 0.08))