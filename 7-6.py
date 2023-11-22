# Using a conditional test in the while statement
age = ""
while age != 'quit':
    age = input("Enter your age (type 'quit' to exit): ")
    
    if age == 'quit':
        break  # Exit the loop if 'quit' is entered
    
    try:
        age = int(age)
        if age < 3:
            print("Your ticket is free.")
        elif 3 <= age <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
    except ValueError:
        print("Invalid input. Please enter a number or 'quit'.")
