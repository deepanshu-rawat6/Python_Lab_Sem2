class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f'The seating capacity of the {self.name} is {capacity} passengers '


class Bus(Vehicle):
    color = "white"

    def __init__(self):
        super().__init__("Bus", "100 km/hr", "5 km/ltr")

    def display(self):
        print("Max speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print(super().seating_capacity(50))
        print("Color of the bus:", self.color)


obj = Bus()
obj.display()
