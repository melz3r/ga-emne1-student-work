def read_guess():
    user_guess = int(input("Guess a number (1-30): "))
    return user_guess

def check_guess(guess, secret_number):
    if guess == secret_number:
        return "correct"
    elif guess < secret_number:
        return "low"
    else:
        return "high"

def show_feedback(result):
    """Print correct/low/high guess-feedback
    for the player."""
    if result == "correct":
        print("Correct number!")
    elif result == "low":
        print("Guess is too low, try again!")
    elif result == "high":
        print("Guess is too high, try again!")
    else:
        print(f'Error, invalid result: "{result}"')