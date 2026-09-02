username = input("Username: ")

is_blocked = False

if username.strip() != "":
    has_username = True
    rules = input("Do you accept the rules? Y or N: ")
    if rules == "Y" or rules == "y":
        accepted_rules = True
    else:
        accepted_rules = False
else:
    has_username = False
    accepted_rules = False

if has_username == True and accepted_rules == True and is_blocked == False:
    print(f"Welcome to the game, {username}.")
else:
    print("You shall not pass!")