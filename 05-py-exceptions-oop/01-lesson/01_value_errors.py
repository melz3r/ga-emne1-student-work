is_input_ok = False
age = 0

while not is_input_ok:
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Error: Only integers are valid")
    else:
        is_input_ok = True

print(f"Next year: {age + 1}")

print("Done.")


