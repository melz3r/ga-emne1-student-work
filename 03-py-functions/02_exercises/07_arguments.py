def show_profile(name, age, city):
    print(f"{name}, {age}, {city}")


show_profile(40, "Ola", "Hamar")
show_profile("Hamar", "Ola", 40)
show_profile("Ola", 40, "Hamar")

# Det siste kallet er riktig. Når man bytter ut rekkefølgen på argumentene, blir bare verdiene endret.
# Noterer meg at det stilles ikke noe krav til hva slags datatype de ulike parametrene er i et slikt oppsett.