def read_number():
    number = int(input("Skriv inn et heltall: "))
    return number

def describe_sign(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

def is_even(number):
    return number % 2 == 0

def show_analysis(number, sign, even):
    print(f"Tall: {number}")
    print(f"Fortegn: {sign}")
    print(f"Partall: {even}")

def run_number_analyzer():
    number = read_number()
    sign = describe_sign(number)
    even = is_even(number)

    show_analysis(number, sign, even)

run_number_analyzer()