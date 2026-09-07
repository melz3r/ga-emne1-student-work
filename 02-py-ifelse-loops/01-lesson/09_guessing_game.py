secret_number = 21
attempts_left = 5
guessed_correctly = False

while attempts_left > 0 and not guessed_correctly:
        user_guess = int(input("Guess the number (1-50): "))
        if user_guess == secret_number:
            print("Success!")
            guessed_correctly = True
        elif user_guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
        attempts_left -= 1

if not guessed_correctly:
    print(f"The number was {secret_number}")

