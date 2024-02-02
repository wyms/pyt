class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Create an instance of the User class
user = User("John", "Doe", 30, "johndoe@example.com")

# Increment login_attempts several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Number of login attempts: {user.login_attempts}")

# Reset login_attempts
user.reset_login_attempts()
print(f"Number of login attempts after reset: {user.login_attempts}")
