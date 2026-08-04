class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand 
        self.model = model 
        self.year = year
    
class Car(Vehicle):
    def __init__(self, brand, model, year, doors, wheels):
        super().__init__(brand, model, year)
        self.doors = doors 
        self.wheels = wheels 

class Bike(Vehicle):
    def __init__(self, brand, model, year, speed):
        super().__init__(brand, model, year)
        self.speed = speed

class Future(Vehicle):
    def __init__(self, brand, model, year, price):
        super().__init__(brand, model, year)
        self.price = price

listt = [
    Car("Suzuki", "Dzire", 2018, 4, 4),
    Car("Suzuki", "XL6", 2021, 4, 4),
    Car("Suzuki", "Fronx", 2024, 4, 4),
    Bike("Honda", "Shine", "2013", 110),
    Bike("Kawaski", "Boxer", "1998", 100),
    Bike("Honda", "Activa", "2016", 100),
    Future("Royal Enfield", "Innterceptor", 2027, 400000)
]

for i in listt:
    print(i.__dict__)