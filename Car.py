class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def test_drive():
        return f" static method to test drive the car."  

    def start_engine(self):
        return f"The {self.color} {self.year} {self.make} {self.model}'s engine has started."

# Example usage:
# my_car = Car("Toyota", "Corolla", 2020, "blue")
# print(my_car.start_engine())
