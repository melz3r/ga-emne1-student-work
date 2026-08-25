temperature_morning = float(input("Registrér morgentemperatur: "))
temperature_evening = float(input("Registrér kveldstemperatur: "))
temperature_average = (temperature_evening + temperature_morning) / 2


print(f"Gjennomsnittstemperaturen er {temperature_average} °C")