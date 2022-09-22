class Food:  # Base Class
    def __init__(self, name, amount):
        self.food = name
        self.amount = amount
        print(f"{self.food} {self.amount} Is Created From Base Class ")

    def eat(self):
        print("Eat Method From Base Class")


class Apple(Food):  # Derived Class
    def __init__(self, name, price, amount):
        self.price = price
        # Food.__init__(self, name)
        super().__init__(name, amount)
        print(f"Is {name} and {price} {amount + 20} Created From Derived Class")

    def eat(self): # override
        print("Eat Method From Derived Class")


food_one = Food("banana", 20)
food_two = Apple("Pizza", 22, 50)
food_two.eat()
