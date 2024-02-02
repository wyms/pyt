class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Create an instance of the Restaurant class
restaurant = Restaurant("Pizza Palace", "Italian")

# Print the attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Call the methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Create three instances of the Restaurant class
restaurant1 = Restaurant("Pho House", "Vietnamese")
restaurant2 = Restaurant("Taco Shack", "Mexican")
restaurant3 = Restaurant("Sushi Star", "Japanese")

# Call describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

# Create several instances of the User class
user1 = User("Alice", "Smith", 30, "alice@example.com")
user2 = User("Bob", "Johnson", 25, "bob@example.com")
user3 = User("Charlie", "Brown", 40, "charlie@example.com")

# Call describe_user() and greet_user() for each instance
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()



# Exercise 9-6: Ice Cream Stand
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(flavor)

# Exercise 9-7: Admin
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, age, email, privileges):
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges(privileges)

# Exercise 9-8: Battery Upgrade (assuming ElectricCar and Battery classes are defined elsewhere)
class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    # ... other methods

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

# Exercise 9-9: Using Battery Upgrade
class ElectricCar:
    def __init__(self, make, model, year):
        # ... other attributes
        self.battery = Battery()

    def get_range(self):
        # Calculate and return the car's range based on battery capacity and other factors
        # Replace this placeholder with your actual range calculation logic
        return 250  # Example placeholder value
    


# Example usage
ice_cream_stand = IceCreamStand("Mike's Ice Cream", "Ice Cream")
ice_cream_stand.flavors = ["Chocolate", "Vanilla", "Strawberry"]
ice_cream_stand.display_flavors()

admin = Admin("John", "Doe", 35, "johndoe@example.com", ["can add post", "can delete post", "can ban user"])
admin.privileges.show_privileges()

my_car = ElectricCar("Tesla", "Model S", 2023)
print(my_car.get_range())  # Initial range
my_car.battery.upgrade_battery()
print(my_car.get_range())  # Range after upgrade
