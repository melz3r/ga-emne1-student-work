import math


def calculate_hypotenuse(side_a, side_b):
    return f"{math.sqrt(side_a ** 2 + side_b **2):.2f}"

print(calculate_hypotenuse(3, 4))
print(calculate_hypotenuse(5, 7))
print(calculate_hypotenuse(2, 2))