import random

def roll_dice(sides = 6):
    return random.randint(1, sides)

for number in range(1, 11):
    print(f"Kast nummer {number} med 6 sider: {roll_dice()}")

print(f"Kast med 20 sider: {roll_dice(20)}")