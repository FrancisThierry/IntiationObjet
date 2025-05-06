from Axle import Axle

class BetterCarWithProp:
    def __init__(self, make, model, year, axle: Axle):
        self._make = make
        self._model = model
        self._year = year
        self._axle = axle
        self._color = None

    # Property pour make
    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        self._make = value

    # Property pour model
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    # Property pour year
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    # Property pour color
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    # Property readonly pour axle
    @property
    def axle(self):
        return self._axle

    @staticmethod
    def test_drive():
        return "Static method to test drive the car."

    def start_engine(self):
        return f"The {self.color} {self.year} {self.make} {self.model}'s engine has started."

# Example usage:
# my_car = BetterCar("Toyota", "Corolla", 2020, Axle())
# my_car.color = "blue"
# print(my_car.start_engine())
