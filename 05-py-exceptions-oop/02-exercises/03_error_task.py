try:
    minutes = int(input("Minutes: "))
except ValueError:
    print("Please enter a whole number.")
else:
    print(f"Seconds: {minutes * 60}")
print("Finished.")


# Finished vises i begge tilfellene da den ligger på samme innrykk som try/except/else og vil uansett bli kjørt etter
# denne blokken. Utskriften av sekunder ligger i else-blokken fordi denne blokken kjøres når det ikke oppstår en
# ValueError, det vil si når konverteringen til int lykkes.