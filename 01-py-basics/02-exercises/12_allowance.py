work_hours = float(input("Skriv inn hvor mange timer du har jobbet: "))
hourly_rate = float(input("Skriv inn din timelønn: "))
pay = work_hours * hourly_rate

print(f"Du har tjent kr {pay:.2f},-")
