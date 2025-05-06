from Axle import Axle

class BetterCar:
    def __init__(self, make, model, year, axle: Axle):
        self.__make = make
        self.__model = model
        self.__year = year
        self.axle = axle

    # Getter et setter pour make
    def get_make(self):
        return self.__make

    def set_make(self, value):
        self.__make = value

    # Getter et setter pour model
    def get_model(self):
        return self.__model

    def set_model(self, value):
        self.__model = value

    # Getter et setter pour year
    def get_year(self):
        return self.__year

    def set_year(self, value):
        self.__year = value

    # Getter et setter pour color
    def get_color(self):
        return "red"

    # def set_color(self, value):
    #     self.__color = value

    def test_drive():
        return f" static method to test drive the car."  

    def start_engine(self):
        return f"The {self.get_color()} {self.get_year()} {self.get_make()} {self.get_model()}'s engine has started."

# Example usage:
# my_car = BetterCar("Toyota", "Corolla", 2020, 200, 4)
# my_car.set_color("blue")
# print(my_car.start_engine())
