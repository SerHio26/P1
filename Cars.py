
class Car:
    def __init__(self, model, yo, engine, price, km, wheels = 4):
        self.model = model
        self.yo = yo
        self.engine = engine
        self.price = price
        self.km = km
        self.wheels = wheels

    def description(self):
        description = (f"Модель автомобиля - {self.model}, Год выпуска - {self.yo}, объём двигателя - {self.engine}, "
                       f"стоимость - {self.price}, пробег - {self.km}, колёс - {self.wheels}")
        return description

class Truck(Car):
    def __init__(self, model, yo, engine, price, km, wheels = 8):
        super().__init__(model, yo, engine, price, km)
        self.wheels = wheels

    def description(self):
        description = (f"Модель автомобиля - {self.model}, Год выпуска - {self.yo}, объём двигателя - {self.engine}, "
                       f"стоимость - {self.price}, пробег - {self.km}, колёс - {self.wheels}")
        return description

car = Car("Mazda", 2023, 2000, "1500$", 10000)
truck = Truck("Catterpillar", 2020, 10000, "25000$", 15000)

print(car.description())
print(truck.description())