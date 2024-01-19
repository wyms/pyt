# 9-4. Number Served
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # New attribute with a default value of 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

# Create an instance and demonstrate number_served methods
restaurant = Restaurant("Best Bites", "Italian")
print(f"Number of customers served: {restaurant.number_served}")

# Change the number of customers served and print again
restaurant.number_served = 50
print(f"Number of customers served: {restaurant.number_served}")

# Use set_number_served() method
restaurant.set_number_served(100)
print(f"Number of customers served: {restaurant.number_served}")

# Use increment_number_served() method
restaurant.increment_number_served(20)
print(f"Number of customers served: {restaurant.number_served}")

