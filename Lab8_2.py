class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def drive(self):
        print(f"Driving the {self.model} {self.make}")

my_car = Car('Ford', 'Mustang')
my_car.drive()