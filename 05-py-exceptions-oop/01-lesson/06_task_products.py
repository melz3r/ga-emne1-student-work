# class Product
# data: name & price
# functionality: show information for this product
#                Apple: 12.00

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(f"Creating {name}...")

    def show_info(self):
        print(f"{self.name}: {self.price:.2f}")

apple = Product("Apple", 12)
bread = Product("Bread", 35)
milk = Product("Milk", 24)

apple.show_info()
bread.show_info()
milk.show_info()

apple.price = 10
apple.show_info()

milk.price = 20
milk.name = "Mjølk"
milk.show_info()