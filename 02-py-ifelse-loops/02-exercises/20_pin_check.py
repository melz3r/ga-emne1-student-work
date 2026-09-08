secret_pin = 2468
attempts_left = 3
is_authenticated = False

while attempts_left > 0 and not is_authenticated:
    user_pin = int(input("Oppgi PIN: "))
    if user_pin == secret_pin:
        print("Welcome.")
        is_authenticated = True
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print(f"Feil pin, prøv igjen. Du har igjen {attempts_left} forsøk.")
if not is_authenticated:
    print("Antall forsøk oppbrukt.")