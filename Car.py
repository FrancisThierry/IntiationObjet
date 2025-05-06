
from Axle import Axle
class Car:
    def __init__(self, make, model, year, color, length:int, number:int):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.axle:Axle = Axle(length=length, number=number)

    def test_drive():
        return f" static method to test drive the car."  

    def start_engine(self):
        return f"The {self.color} {self.year} {self.make} {self.model}'s engine has started."

# Example usage:
# my_car = Car("Toyota", "Corolla", 2020, "blue")
# print(my_car.start_engine())
