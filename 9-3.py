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
