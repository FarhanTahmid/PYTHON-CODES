class Car:
    def __int__(self, make, model, year):
        self.manufacturer = make
        self.carModel = model
        self.year = year
        self.odometerReading = 0.0

    def getDetailsOfCar(self):
        longName = f"Manufacturer {self.manufacturer}, Model {self.carModel}, year {self.year}"
        return longName.title()

    def getOdometerReading(self):
        return self.odometerReading

    def updateOdometer(self, mileage):
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back mileage")

    def incrementOdometer(self, miles):
        self.odometerReading += miles


myCar = Car('Audi','R8',2022)
print(myCar.getDetailsOfCar())


class ElectricCars(Car):
    def __init__(self, make, model, year):
        #super().__init__(make, model, year)
        self.battery = 80


newTesla = ElectricCars('Tesla', 'Model S', 2019)
print(newTesla.battery)
print(newTesla.getDetailsOfCar())