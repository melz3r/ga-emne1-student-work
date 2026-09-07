temperature_morning = float(input("Registrér morgentemperatur i Celsius: "))
temperature_evening = float(input("Registrér kveldstemperatur i Celsius: "))
temperature_average_celsius = (temperature_evening + temperature_morning) / 2
temperature_average_fahrenheit = temperature_average_celsius * 9 / 5 + 32

print(f"Gjennomsnittstemperaturen er {temperature_average_celsius:.1f} °C eller {temperature_average_fahrenheit:.1f} °F")