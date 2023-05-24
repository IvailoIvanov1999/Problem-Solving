class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money, owner):
        self.money = money
        self.owner = owner

        if self.money >= self.price and self.owner == None:
            return (f"Successfully bought a {self.type}. Change: {float((self.money - self.price)):.2f}")

        elif self.owner != None:
            return "Car already sold"

        else:
            return "Sorry, not enough money"

    def sell(self):
        if self.owner != None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner != None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
