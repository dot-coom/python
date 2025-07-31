class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def details(self):
        print(f"Name: {self.name}, Color: {self.color}, Price: {self.price}")

class Four_Wheeler:
    def __init__(self, name, color, wheel_type):
        self.name = name
        self.color = color
        self.wheel_type = wheel_type

    def fw_details(self):
        print(f"Name: {self.name}, Color: {self.color}, Wheel_Type: {self.wheel_type}")

class Car(Vehicle, Four_Wheeler):
    def __init__(self, name, color, price, wheel_type, model):
        Vehicle.__init__(self, name, color, price)
        Four_Wheeler.__init__(self, name, color, wheel_type)
        self.model = model

    def car_details(self):
        Vehicle.details(self)
        Four_Wheeler.fw_details(self)
        print(f"Model: {self.model}")

car1 = Car("Honda", "White", 1700000, "Alloy + Carbon_Fibre", "2025")
car1.car_details()
        