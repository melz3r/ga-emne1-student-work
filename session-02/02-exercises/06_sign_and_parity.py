integer = int(input("Heltall: "))

modulus = integer % 2

if integer > 0:
    print("Tallet er større enn null.")
    if modulus == 0:
        print("Tallet er et partall.")
    elif modulus != 0:
        print("Tallet er et oddetall.")
elif integer < 0:
    print("Tallet er mindre enn null.")
    if modulus == 0:
        print("Tallet er et partall.")
    elif modulus != 0:
        print("Tallet er et oddetall.")
else:
    print("Tallet er null.")



