class Car:
    def __int__(self, make, model, year):
        self.manufacturer = make
        self.carModel = model;
        self.year = year
        self.odometerReading = 0.0

    def getDetailsOfCar(self):
        print(f"Manufacturer {self.manufacturer}, Model {self.carModel}, year {self.year}")

    def getOdometerReading(self):
        return self.odometerReading

    def updateOdometer(self, mileage):
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back mileage")

    def incrementOdometer(self, miles):
        self.odometerReading += miles


class ElectricCars(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)


newTesla = ElectricCars('Tesla', 'Model S', 2019)
newTesla.getDetailsOfCar()
