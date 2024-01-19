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

# 9-3. Users
class User:
    def __init__(self, first_name, last_name, age, gender, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.location = location

    def describe_user(self):
        print(f"User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

# Create instances representing different users
user1 = User("John", "Doe", 25, "Male", "New York")
user2 = User("Alice", "Johnson", 30, "Female", "Los Angeles")
user3 = User("Bob", "Smith", 22, "Male", "Chicago")

# Call methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
