class Bike:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def bike_info(self):
        return f"{self.year} {self.brand} {self.model}"

    def bike_age(self, current_year):
        return current_year - self.year