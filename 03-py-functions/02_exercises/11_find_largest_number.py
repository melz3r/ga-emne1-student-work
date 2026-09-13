def find_largest(first_number, second_number):
    if first_number > second_number:
        return f"{first_number} er større enn {second_number}"
    elif first_number < second_number:
        return f"{second_number} er større enn {first_number}"
    else:
        return "Tallene er like."

print(find_largest(5, 10))
print(find_largest(20, 7))
print(find_largest(8, 8))