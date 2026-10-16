""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
""" 

Create a class hierarchy:
 
    Base class Vehicle with attributes: brand, model, year

    Derived class Car with additional attribute: number_of_doors

    Implement a method get_info() in both classes
 
"""
class Vehicle:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"


class Car(Vehicle):

    def __init__(self, brand, model, year, number_of_doors): 
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        # 2. หรือจะใช้ super().get_info() + ต่อท้ายด้วย doors ก็ได้เช่นกัน
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Number of doors: {self.number_of_doors}"


# --- การเรียกใช้งาน (อยู่นอกคลาส) ---
vehicle = Vehicle("Toyota", "Yaris", "2025")
print(vehicle.get_info())

car = Car("Toyota", "Yaris", "2025", "5")
print(car.get_info())