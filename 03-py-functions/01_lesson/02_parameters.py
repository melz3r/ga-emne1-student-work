def greet(name):
    print(f"Hello, {name}!")


def show_total(price, quantity):
    total = price * quantity
    print(f"Total: kr {total:.2f}")


greet("Ola")
greet("Knut")
greet("Kåre")
greet("Lars")

show_total(399.90, 3)