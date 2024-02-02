class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_by):
        self.number_served += increment_by

# Create an instance of the Restaurant class
restaurant = Restaurant("Pizza Palace", "Italian")

# Print the initial number of customers served
print(f"Number of customers served: {restaurant.number_served}")

# Set the number_served using set_number_served()
restaurant.set_number_served(40)
print(f"Number of customers served after setting: {restaurant.number_served}")

# Increment the number_served using increment_number_served()
restaurant.increment_number_served(25)
print(f"Number of customers served after incrementing: {restaurant.number_served}")
