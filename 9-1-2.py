# 9-1. Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Create an instance and call methods
restaurant = Restaurant("Best Bites", "Italian")
print(f"Restaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2. Three Restaurants
restaurant1 = Restaurant("Tasty Treats", "Mexican")
restaurant2 = Restaurant("Spicy Delight", "Indian")
restaurant3 = Restaurant("Sushi Heaven", "Japanese")

# Call describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# Open the 3 restaurants
restaurant1.open_restaurant()
restaurant2.open_restaurant()
restaurant3.open_restaurant()
