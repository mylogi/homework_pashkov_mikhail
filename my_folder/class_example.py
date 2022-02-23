class Car:
    total_number_of_car = 0

    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.total_driven_km = 0
        Car.total_number_of_car += 1

    def repaint(self, color):
        self.color = color

    def drive(self, km_driven):
        self.total_driven_km += km_driven

    def __repr__(self):
        return f'{self.brand}, {self.model} {self.year} {self.color}'

    def __str__(self):
        return f'{self.brand} {self.model} - {self.year}'


class Truck(Car):

    def __init__(self, brand, model, year, color, trailers):
        super().__init__(brand, model, year, color)
        self.trailers = trailers

    def attach_trailer(self, num_of_trailers=1):
        self.trailers += num_of_trailers

    def detach_trailers(self, num_of_trailers=1):
        self.trailers -= num_of_trailers
