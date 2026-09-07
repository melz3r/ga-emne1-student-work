integer = int(input("Heltall: "))

modulus = integer % 2

if integer > 0:
    print("Tallet er større enn null.")
elif integer < 0:
    print("Tallet er mindre enn null.")
else:
    print("Tallet er null.")

if integer != 0:
    if modulus == 0:
        print("Tallet er et partall.")
    else:
        print("Tallet er et oddetall.")

