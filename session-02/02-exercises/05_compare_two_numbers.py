first_number = int(input("Første heltall: "))
second_number = int(input("Andre heltall: "))

if first_number == second_number:
    print("Tallene er like.")
elif first_number > second_number:
    print(f"{first_number} er større enn {second_number}")
else:
    print(f"{second_number} er større enn {first_number}")