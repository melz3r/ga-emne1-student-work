minutes = int(input("Hvor mange minutter skal du studere i dag? Skriv inn et helt tall: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"Dette tilsvarer {hours} timer og {remaining_minutes} minutter.")