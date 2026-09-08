number = int(input("Skriv inn et positivt heltall: "))


while number > 0:
    print(f"Du skrev {number}")
    number = int(input("Skriv inn et nytt positivt tall (0 eller negativt tall for å avslutte): "))
print(f"Programmet avsluttes fordi du skrev {number}")


