class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh!")

class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

    # ... (Other methods from electric_car.py)

# Example usage
car = ElectricCar("Tesla", "Model S", 2023)
car.battery.describe_battery()
car.battery.upgrade_battery()
car.battery.describe_battery()
