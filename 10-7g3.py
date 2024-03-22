# Exercise 10-7: Addition Calculator
def addition_calculator():
    while True:
        add_numbers()
        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != 'yes':
            break
