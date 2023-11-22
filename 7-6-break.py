# Using a break statement
while True:
    age = input("Enter your age (type 'quit' to exit): ")
    if age.lower() == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
