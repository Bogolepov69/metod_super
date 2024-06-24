class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = None

class Car (Vehicle):
    def __init__(self, prise):
        self.price = 1000000
    def horse_powers(self):
        return f"Лошадиных сил: {self.horse_powers}"


class Nissan (Car, Vehicle):
    def __init__(self, vehicle_type, price, horse_powers):
        self.vehicle_type = "sedan"
        self.price = 2000000
        self.horse_powers = 200



nissan = Nissan('sedan', 200000, 200)

print(nissan.vehicle_type)
print(nissan.price)
print(nissan.horse_powers)