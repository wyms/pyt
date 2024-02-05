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


class Admin(User):
    def __init__(self, first_name, last_name, age, gender, location, privileges):
        super().__init__(first_name, last_name, age, gender, location)
        self.privileges = privileges

    def show_privileges(self):
        print(f"Admin {self.first_name} {self.last_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Example usage (corrected)
admin = Admin("John", "Doe", 30, "Male", "New York", ["can add post", "can delete post", "can ban user"])
admin.show_privileges()
