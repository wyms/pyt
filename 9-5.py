# 9-5. Login Attempts
class User:
    def __init__(self, first_name, last_name, age, gender, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.location = location
        self.login_attempts = 0  # New attribute

    def describe_user(self):
        print(f"User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Create an instance and demonstrate login_attempts methods
user = User("John", "Doe", 25, "Male", "New York")

# Increment login attempts and print the value
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login Attempts: {user.login_attempts}")

# Reset login attempts and print again
user.reset_login_attempts()
print(f"Login Attempts (after reset): {user.login_attempts}")
