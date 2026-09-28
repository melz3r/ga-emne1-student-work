valid_input = False

while not valid_input:
    user_input_tickets = 0
    try:
        user_input_tickets = input("Hvor mange billetter ønsker du? ")
        number_of_tickets = int(user_input_tickets)
        print(f"Printer {number_of_tickets} billetter.")
        valid_input = True
    except ValueError:
        print(f"{user_input_tickets} er ikke et heltall. Prøv igjen.")