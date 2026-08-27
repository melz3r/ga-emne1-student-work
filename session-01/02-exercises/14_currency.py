amount = float(input("Skriv inn et beløp i NOK: "))
rate = float(input("Skriv inn valutakursen (hvor mye 1 NOK er verdt i målvalutaen): "))

result = amount * rate

print(f"Resultat: {result:.2f} NOK")