distance_in_km = float(input("Kjørelengde i km: "))
fuel_per_100_km = float(input("Drivstoff-forbruk per 100 km: "))
fuel_price = float(input("Drivstoffpris per liter: "))

#Forventet leveranse: Et program som skriver ut drivstoffmengde og kostnad med forklarende tekst.


fuel_per_km = fuel_per_100_km / 100
fuel_usage = fuel_per_km * distance_in_km
total_cost = fuel_usage * fuel_price

print(f"Drivstoff-forbruk for kjøreturen: {fuel_usage} liter")
print(f"Kostnad for kjøreturen: {total_cost:.2f} kr")