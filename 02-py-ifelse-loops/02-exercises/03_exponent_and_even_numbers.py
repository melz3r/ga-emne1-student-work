integer = int(input("Heltall: "))

integer_to_the_power_of_two = integer ** 2
integer_to_the_power_of_three = integer ** 3
integer_modulus = integer % 2

print(f"Tallet opphøyd i andre: {integer_to_the_power_of_two}")
print(f"Tallet opphøyd i tredje: {integer_to_the_power_of_three}")
print(f"Rest når heltallet deles på 2: {integer_modulus}")