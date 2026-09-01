first_number = int(input("Første heltall: "))
second_number = int(input("Andre heltall: "))

total_sum = first_number + second_number
difference = first_number - second_number
product = first_number * second_number

print(f"Sum: {total_sum}")
print(f"Difference: {difference}")
print(f"Product: {product}")

if second_number != 0:
    division = first_number / second_number
    int_division = first_number // second_number
    modulus = first_number % second_number

    print(f"Division: {division}")
    print(f"Integer division: {int_division}")
    print(f"Rest: {modulus}")
else:
    print("Division: Kan ikke dele på 0")
    print("Integer division: Kan ikke dele på 0")
    print("Rest: Kan ikke dele på 0")

# Uten en if-else her, får vi feilmeldingen
# "ZeroDivisionError: division by zero"
# når second_number er 0.
# Dette fordi man ikke kan dele et tall på 0.