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
